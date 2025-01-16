"""
Tests for Pydantic schemas.
"""

from app.schemas import UserResponse, UserAuditResponse
from datetime import datetime, timezone


def test_user_response_schema():
    user_data = {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}
    user = UserResponse(**user_data)
    assert user.id == 1
    assert user.name == "John Doe"


def test_user_audit_response_schema():
    audit_data = {
        "id": 1,
        "user_id": 1,
        "operation": "create",
        "timestamp": datetime.now(timezone.utc),  # Use timezone-aware datetime
        "previous_data": {},
        "new_data": {"name": "John Doe"},
    }
    audit = UserAuditResponse(**audit_data)
    assert audit.operation == "create"