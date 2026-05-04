from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import engine, get_db, Base
from model import TransactionModel
from schemas import Transaction, TransactionResponse
from rules import check_rules
from ml import predict_fraud
from utils import calculate_final_risk
from logging_config import setup_logging
from auth import create_token

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Real-Time Fraud Detection",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
    openapi_tags=[]
)

# Enable CORS (required for dashboard)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize logger
logger = setup_logging()


# ---------------------------
# HOME
# ---------------------------

@app.get("/")
def home():
    return {
        "message": "Fraud Detection System Running"
    }


# ---------------------------
# LOGIN
# ---------------------------

@app.post("/login")
def login(username: str, password: str):

    if username == "admin" and password == "admin123":

        token = create_token(username)

        return {
            "access_token": token
        }

    return {
        "error": "Invalid credentials"
    }


# ---------------------------
# PROCESS TRANSACTION
# ---------------------------

@app.post(
    "/transaction",
    response_model=TransactionResponse
)
def process_transaction(
    transaction: Transaction,
    db: Session = Depends(get_db)
):

    # Rule-based risk
    rule_risk = check_rules(transaction)

    # ML prediction
    prediction = predict_fraud(
        transaction.amount
    )

    # Final risk
    final_risk = calculate_final_risk(
        rule_risk,
        prediction
    )

    # Decision
    if final_risk > 0.7:
        status = "blocked"
    else:
        status = "approved"

    # Save to database
    db_transaction = TransactionModel(
        user_id=transaction.user_id,
        amount=transaction.amount,
        location=transaction.location,
        device=transaction.device,
        risk_score=final_risk,
        status=status
    )

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    # Logging
    logger.info(
        f"User {transaction.user_id} | "
        f"Amount {transaction.amount} | "
        f"Status {status} | "
        f"Risk {final_risk}"
    )

    return {
        "status": status,
        "risk_score": final_risk
    }


# ---------------------------
# TRANSACTION HISTORY
# ---------------------------

@app.get("/transactions")
def get_transactions(
    db: Session = Depends(get_db)
):

    transactions = db.query(
        TransactionModel
    ).all()

    return transactions