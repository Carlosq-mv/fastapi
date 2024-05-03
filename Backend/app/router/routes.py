from fastapi import APIRouter
from typing import List
from app.schema import TransactionBase, TransactionModel
from app.dependencies import db_dependency
from app import models

transaction_routes = APIRouter()

@transaction_routes.post('/', response_model=TransactionModel)
async def create_transaction(transaction: TransactionBase, db: db_dependency):
    db_transaction = models.Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@transaction_routes.get('/', response_model=List[TransactionModel])
async def read_transactions(db: db_dependency, skip: int = 0, limit: int = 100):
    transactions = db.query(models.Transaction).offset(skip).limit(limit).all()
    return transactions