from sqlalchemy.orm import Session
from .model import Employee

def create_employee(db: Session, data):
    employee = Employee(**data.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def get_employee(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()


def update_employee(db: Session, emp_id: int, data):
    emp = get_employee(db, emp_id)
    for k, v in data.dict(exclude_unset=True).items():
        setattr(emp, k, v)
    db.commit()
    return emp


def delete_employee(db: Session, emp_id: int):
    emp = get_employee(db, emp_id)
    db.delete(emp)
    db.commit()
