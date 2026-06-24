from fastapi import APIRouter, HTTPException, status
from models import Transaction, TransactionCreate, Customer
from db import SessionDep
from sqlmodel import select


router = APIRouter()


@router.post("/transactions", response_model=Transaction, tags=["transactions"])
async def create_transaction(transaction_data: TransactionCreate, session: SessionDep):
    # Convertir a dict
    transaction_dict = transaction_data.model_dump()
    
    # Verificar que el customer existe
    customer = session.get(Customer, transaction_dict.get("customer_id"))
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Customer not found"
        )
    
    # Crear objeto SQLModel
    transaction_db = Transaction.model_validate(transaction_dict)
    
    # Guardar en DB
    session.add(transaction_db)
    session.commit()
    session.refresh(transaction_db)
    
    return transaction_db  # Retorna el objeto SQLModel (FastAPI lo convierte a JSON)

    


@router.get("/transactions", status_code=status.HTTP_201_CREATED, tags=["transactions"])
async def list_transaction(session: SessionDep):
    query = select(Transaction)
    transactions = session.exec(query).all()
    return transactions
    