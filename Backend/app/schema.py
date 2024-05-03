from pydantic import BaseModel  # data validations
from app.database import SessionLocal

# pydantic model: validate request from React app -- if data is valid accept into FastApi app or reject request if not valid
class TransactionBase(BaseModel):
    amount: float
    category: str
    description: str
    is_income: bool
    date: str
    
class TransactionModel(TransactionBase):
    id: int
    class Config:
        orm_mode=True
        
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
