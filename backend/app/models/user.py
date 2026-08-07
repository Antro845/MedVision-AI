from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    fullname = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    role = Column(
        String(20),
        default="PATIENT",
        nullable=False
    )

    phone = Column(
        String(20),
        nullable=True
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

    images = relationship(
    "MedicalImage",
    back_populates="user"
)
    patient_cases = relationship(
    "MedicalCase",
    foreign_keys="MedicalCase.patient_id"
)
    doctor_cases = relationship(
    "MedicalCase",
    foreign_keys="MedicalCase.doctor_id"
)