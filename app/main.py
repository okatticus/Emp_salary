from fastapi import FastAPI
from app.database import Base, engine
from app.routes import employee, metrics

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(employee.router)
app.include_router(metrics.router)

#python -m uvicorn app.main:app --reload