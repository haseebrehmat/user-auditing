"""
Service layer for audit operations.
"""

from sqlalchemy.orm import Session
from app.models import UserAudit


def fetch_audit_logs(db: Session):
    """Fetch all audit logs."""
    return db.query(UserAudit).all()
