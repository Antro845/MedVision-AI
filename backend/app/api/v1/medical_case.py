from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi import APIRouter, Depends
from app.database.database import get_db



from app.schemas.medical_case import (
    MedicalCaseCreate,
    MedicalCaseUpdate,
    MedicalCaseResponse,
)

from app.services.medical_case_service import (
    create_case,
    get_all_cases,
    get_case_by_id,
    update_case,
    delete_case,
    discharge_case,
)

router = APIRouter()

@router.get("/cases", response_model=list[MedicalCaseResponse])
def get_cases(db: Session = Depends(get_db)):
    return get_all_cases(db)

@router.get("/cases/{case_id}", response_model=MedicalCaseResponse)
def get_case(case_id: int, db: Session = Depends(get_db)):
    medical_case = get_case_by_id(db, case_id)

    if not medical_case:
        raise HTTPException(status_code=404, detail="Medical case not found")

    return medical_case

@router.delete("/{case_id}")
def delete_medical_case(
    case_id: int,
    db: Session = Depends(get_db)
):
    return delete_case(db, case_id)



@router.put("/cases/{case_id}", response_model=MedicalCaseResponse)
def update_medical_case(
    case_id: int,
    case_update: MedicalCaseUpdate,
    db: Session = Depends(get_db),
):
    medical_case = update_case(
        db=db,
        case_id=case_id,
        diagnosis=case_update.diagnosis,
        status=case_update.status,
    )

    if not medical_case:
        raise HTTPException(
            status_code=404,
            detail="Medical case not found"
        )

    return medical_case

@router.post("/cases",response_model=MedicalCaseResponse)
def create_medical_case(
    case: MedicalCaseCreate,
    db: Session = Depends(get_db)
):
    return create_case(
        db=db,
        patient_id=case.patient_id,
        doctor_id=case.doctor_id,
        diagnosis=case.diagnosis
    )
   
@router.patch("/{case_id}/discharge", response_model=MedicalCaseResponse)
def discharge_medical_case(
    case_id: int,
    db: Session = Depends(get_db),
):
    return discharge_case(db, case_id)
   