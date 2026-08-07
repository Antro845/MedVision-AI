from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class MedicalCase(Base):
    __tablename__ = "medical_cases"

    id = Column(Integer, primary_key=True, index=True)

    case_number = Column(
        String(30),
        unique=True,
        nullable=False
    )

    patient_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    doctor_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    diagnosis = Column(
        String(255),
        nullable=True
    )

    status = Column(
        String(30),
        default="OPEN",
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    discharged_at = Column(
        DateTime,
        nullable=True
    )

    patient = relationship(
    "User",
    foreign_keys=[patient_id],
    back_populates="patient_cases"
)
    doctor = relationship(
    "User",
    foreign_keys=[doctor_id],
    back_populates="doctor_cases"
)