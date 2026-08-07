import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.medical_case import MedicalCase
from fastapi import HTTPException


def generate_case_number():
    return f"CASE-{str(uuid.uuid4())[:8].upper()}"


def create_case(
    db: Session,
    patient_id: int,
    doctor_id: int,
    diagnosis: str = None,
):
    medical_case = MedicalCase(
        case_number=generate_case_number(),
        patient_id=patient_id,
        doctor_id=doctor_id,
        diagnosis=diagnosis,
    )
    db.add(medical_case)
    db.commit()
    db.refresh(medical_case)
    return medical_case

def get_all_cases(db: Session):
    return db.query(MedicalCase).all()

def get_case_by_id(db: Session, case_id: int):
    return db.query(MedicalCase).filter(MedicalCase.id == case_id).first()

def update_case(
    db: Session,
    case_id: int,
    diagnosis: str = None,
    status: str = None,
):
    medical_case = (
        db.query(MedicalCase)
        .filter(MedicalCase.id == case_id)
        .first()
    )

    if not medical_case:
        return None

    if diagnosis is not None:
        medical_case.diagnosis = diagnosis

    if status is not None:
        medical_case.status = status

    medical_case.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(medical_case)

    return medical_case

def delete_case(db: Session, case_id: int):
    case = db.query(MedicalCase).filter(MedicalCase.id == case_id).first()

    if not case:
        raise HTTPException(status_code=404, detail="Medical case not found")

    db.delete(case)
    db.commit()

    return {"message": "Medical case deleted successfully"}

def discharge_case(db: Session, case_id: int):
    case = db.query(MedicalCase).filter(MedicalCase.id == case_id).first()

    if not case:
        raise HTTPException(status_code=404, detail="Medical case not found")

    case.status = "DISCHARGED"
    case.discharged_at = datetime.utcnow()
    case.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(case)

    return case
