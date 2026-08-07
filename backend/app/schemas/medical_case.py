from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MedicalCaseCreate(BaseModel):
    patient_id: int
    doctor_id: int
    diagnosis: Optional[str] = None


class MedicalCaseUpdate(BaseModel):
    diagnosis: Optional[str] = None
    status: Optional[str] = None


class MedicalCaseResponse(BaseModel):
    id: int
    case_number: str
    patient_id: int
    doctor_id: int
    diagnosis: Optional[str]
    status: str
    created_at: datetime
    updated_at: datetime
    discharged_at: Optional[datetime]

    class Config:
        from_attributes = True