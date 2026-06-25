
from fastapi import APIRouter, status
from models import Plan
from db import SessionDep
from sqlmodel import select

router = APIRouter()

@router.post("/plans", status_code=status.HTTP_201_CREATED, response_model=Plan, tags=["plans"])
def create_plan(plan_data: Plan, session: SessionDep):
    plan_db = Plan.model_validate(plan_data.model_dump())
    session.add(plan_db)
    session.commit()
    session.refresh(plan_db)
    return plan_db


@router.get("/plans", response_model=list[Plan], tags=["plans"])
def list_plans(session: SessionDep):
    query = select(Plan)
    plans = session.exec(query).all()
    return plans
