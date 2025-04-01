from pydantic import BaseModel

class Expense(BaseModel):
    id: int
    date: str
    category: str
    has_receipt: str
    description: str
    amount_spent: str