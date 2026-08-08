from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ReportCreate(BaseModel):
    case_id: int
    patient_id: int
    doctor_id: int
    report_type: str
    title: str
    content: str


class ReportUpdate(BaseModel):
    report_type: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None


class ReportResponse(BaseModel):
    id: int
    case_id: int
    patient_id: int
    doctor_id: int
    report_type: str
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True