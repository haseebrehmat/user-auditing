"""
Routes for audit-related operations.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import UserAuditResponse
from app.db.connection import get_db
from app.services.audit_service import fetch_audit_logs

router = APIRouter()


@router.get("/", response_model=list[UserAuditResponse])
def get_audit_logs_route(db: Session = Depends(get_db)):
    return fetch_audit_logs(db)
