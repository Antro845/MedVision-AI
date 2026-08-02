from app.database.database import engine
from sqlalchemy import text
from fastapi import FastAPI
from app.models.user import Base

Base.metadata.create_all(bind=engine)
with engine.connect() as connection:
    connection.execute(text("SELECT 1"))
    print("✅ PostgreSQL Connected Successfully")
app = FastAPI(
    title="MedVision AI",
    version="1.0.0",
    description="Medical Imaging Analysis Platform"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to MedVision AI",
        "status": "Backend Running Successfully"
    }