from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)  # "income" | "expense"
    category = Column(String, nullable=False)
    date = Column(String, nullable=False)  # formato ISO YYYY-MM-DD
    description = Column(String, nullable=True)
