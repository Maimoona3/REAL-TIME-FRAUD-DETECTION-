from sqlalchemy import Column, Integer, Float, String
from database import Base

class TransactionModel(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    amount = Column(Float)
    location = Column(String)
    device = Column(String)
    risk_score = Column(Float)
    status = Column(String)