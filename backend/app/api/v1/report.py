from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.report import (
    ReportCreate,
    ReportUpdate,
    ReportResponse,
)
from app.services.report_service import (
    create_report,
    get_all_reports,
    get_report_by_id,
    update_report,
    delete_report,
)


router = APIRouter()


@router.post(
    "/reports",
    response_model=ReportResponse
)
def create_medical_report(
    report: ReportCreate,
    db: Session = Depends(get_db)
):
    return create_report(db, report)


@router.get(
    "/reports",
    response_model=list[ReportResponse]
)
def get_reports(
    db: Session = Depends(get_db)
):
    return get_all_reports(db)


@router.get(
    "/reports/{report_id}",
    response_model=ReportResponse
)
def get_report(
    report_id: int,
    db: Session = Depends(get_db)
):
    report = get_report_by_id(db, report_id)

    if not report:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return report


@router.put(
    "/reports/{report_id}",
    response_model=ReportResponse
)
def update_medical_report(
    report_id: int,
    report: ReportUpdate,
    db: Session = Depends(get_db)
):
    updated_report = update_report(
        db,
        report_id,
        report
    )

    if not updated_report:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return updated_report


@router.delete("/reports/{report_id}")
def delete_medical_report(
    report_id: int,
    db: Session = Depends(get_db)
):
    deleted_report = delete_report(
        db,
        report_id
    )

    if not deleted_report:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return {
        "message": "Report deleted successfully"
    }