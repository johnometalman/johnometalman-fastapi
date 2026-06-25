from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from models import Customer, CustomerCreate, CustomerUpdate, Plan, CustomerPlan
from db import SessionDep

router = APIRouter()

# db_customers: list[Customer] = []

@router.post("/", response_model=Customer, tags=["customers"])
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@router.get("/customers/{customer_id}", response_model=Customer, tags=["customers"])
async def read_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Customer not found"
        )
    return customer


@router.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED, tags=["customers"])
async def update_customer(customer_id: int, customer_update: CustomerUpdate, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Customer not found"
        )

    update_dict = customer_update.model_dump(exclude_unset=True)
    customer.sqlmodel_update(update_dict)  
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@router.delete("/customers/{customer_id}", tags=["customers"])
async def delete_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Customer not found"
        )
    session.delete(customer)
    session.commit()
    return {"detail": "Customer deleted"}


@router.get("/customers", response_model=list[Customer], tags=["customers"])
async def list_customers(session: SessionDep):
    return session.exec(select(Customer)).all()
    # return db_customers


@router.post("/customers/{customer_id}/plans/{plan_id}", tags=["customers"])
async def subscribe_customer_to_plan(customer_id: int, plan_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Customer does not exists"
        )
    plan_db = session.get(Plan, plan_id)
    if not plan_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Plan does not exists"
        )
    customer_plan_db = CustomerPlan(
        customer_id=customer_db.id,
        plan_id=plan_db.id
    )
    session.add(customer_plan_db)
    session.commit()
    session.refresh(customer_plan_db)
    return customer_plan_db
    

@router.get("/customers/{customer_id}/plans/", tags=["customers"])
async def list_customer_plans(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Customer does not exists"
        )
    return customer_db.plans

    
    