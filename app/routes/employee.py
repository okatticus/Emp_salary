from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
import app.crud as crud
import app.schemas as schemas

from ..salary import calculate_salary

router = APIRouter(prefix="/employees", tags=["employees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=schemas.EmployeeOut, status_code=201)
def create_employee(data: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, data)


@router.get("/{emp_id}", response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = crud.get_employee(db, emp_id)
    if not emp:
        raise HTTPException(404)
    return emp


@router.put("/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, data: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    return crud.update_employee(db, emp_id, data)


@router.delete("/{emp_id}", status_code=204)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    crud.delete_employee(db, emp_id)


@router.get("/{emp_id}/salary")
def salary(emp_id: int, db: Session = Depends(get_db)):
    emp = crud.get_employee(db, emp_id)
    return calculate_salary(emp.country, emp.salary)

