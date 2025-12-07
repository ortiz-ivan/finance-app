from pydantic import BaseModel


class TransactionBase(BaseModel):
    amount: float
    type: str
    category: str
    daate: str
    description: str | None = None


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True
