from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # CORS for React (React can call fastapi)
from app.router.routes import transaction_routes

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    
)

# TODO: app.include_router(transaction_routes, prefix="/transactions/v1", tags=["Transactions"])
# NOTE: Prefix is like how django handles urls -- look into this when structuring project
app.include_router(transaction_routes, prefix="/transactions", tags=["Transactions"])
# app.include_router(transaction_routes, tags=["Transactions"])