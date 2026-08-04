import os
import shutil
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.image import MedicalImage
from app.models.user import User
from app.schemas.image import ImageResponse
from app.core.security import get_current_user

router = APIRouter()

UPLOAD_FOLDER = "app/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/upload", response_model=ImageResponse)
def upload_image(
    image: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    filepath = os.path.join(UPLOAD_FOLDER, image.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    db_image = MedicalImage(
        filename=image.filename,
        filepath=filepath,
        user_id=current_user.id,
    )

    db.add(db_image)
    db.commit()
    db.refresh(db_image)

    return db_image