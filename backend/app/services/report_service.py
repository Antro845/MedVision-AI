from sqlalchemy.orm import Session

from app.models.report import Report
from app.schemas.report import ReportCreate, ReportUpdate


def create_report(db: Session, report_data: ReportCreate):
    report = Report(
        case_id=report_data.case_id,
        patient_id=report_data.patient_id,
        doctor_id=report_data.doctor_id,
        report_type=report_data.report_type,
        title=report_data.title,
        content=report_data.content,
    )

    db.add(report)
    db.commit()
    db.refresh(report)

    return report


def get_all_reports(db: Session):
    return db.query(Report).all()


def get_report_by_id(db: Session, report_id: int):
    return db.query(Report).filter(Report.id == report_id).first()


def update_report(
    db: Session,
    report_id: int,
    report_data: ReportUpdate
):
    report = get_report_by_id(db, report_id)

    if not report:
        return None

    if report_data.report_type is not None:
        report.report_type = report_data.report_type

    if report_data.title is not None:
        report.title = report_data.title

    if report_data.content is not None:
        report.content = report_data.content

    db.commit()
    db.refresh(report)

    return report


def delete_report(db: Session, report_id: int):
    report = get_report_by_id(db, report_id)

    if not report:
        return None

    db.delete(report)
    db.commit()

    return report