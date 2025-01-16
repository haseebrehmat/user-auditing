"""
Tests for service logic.
"""

from app.services.audit_service import fetch_audit_logs
from sqlalchemy.orm import Session


def test_fetch_audit_logs(db_session: Session):
    audits = fetch_audit_logs(db_session)
    assert audits is not None
    assert isinstance(audits, list)
