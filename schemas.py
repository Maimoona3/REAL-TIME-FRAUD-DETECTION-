from pydantic import BaseModel


class Transaction(BaseModel):

    user_id: int
    amount: float
    location: str
    device: str


class TransactionResponse(BaseModel):

    status: str
    risk_score: float