from fastapi import FastAPI
from app.database import engine, Base
from app.routers import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task manager API Modular")

app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "¡API conectada y modularizada siguiendo Clean Code!"}
