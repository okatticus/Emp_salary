from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import SessionLocal
from ..model import Employee

router = APIRouter(prefix="/metrics", tags=["metrics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/country/{country}")
def salary_by_country(country: str, db: Session = Depends(get_db)):
    q = db.query(
        func.min(Employee.salary),
        func.max(Employee.salary),
        func.avg(Employee.salary),
    ).filter(Employee.country == country).one()

    return {"min": q[0], "max": q[1], "avg": q[2]}


@router.get("/job-title/{job_title}")
def salary_by_job_title(job_title: str, db: Session = Depends(get_db)):
    avg = (
        db.query(func.avg(Employee.salary))
        .filter(Employee.job_title == job_title)
        .scalar()
    )
    return {"avg_salary": avg}
