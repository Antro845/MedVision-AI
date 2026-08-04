from fastapi import FastAPI
from sqlalchemy import text
from app.models.image import MedicalImage
from app.database.database import engine
from app.models.user import Base
from app.api.v1.auth import router as auth_router
from app.api.v1.upload import router as upload_router
app = FastAPI(
    title="MedVision AI",
    version="1.0.0",
    description="Medical Imaging Analysis Platform",
    swagger_ui_parameters={
        "persistAuthorization": True
    }
)

app.include_router(
    auth_router,
    prefix="/api/v1",
    tags=["Authentication"]
)

Base.metadata.create_all(bind=engine)

with engine.connect() as connection:
    connection.execute(text("SELECT 1"))
    print("✅ PostgreSQL Connected Successfully")


@app.get("/")
def root():
    return {
        "message": "Welcome to MedVision AI",
        "status": "Backend Running Successfully"
    }
    
app.include_router(
    upload_router,
    prefix="/api/v1",
    tags=["Upload"]
)