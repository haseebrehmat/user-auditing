"""
Tests for SQLAlchemy models.
"""

from app.models import User, UserAudit


def test_user_model():
    user = User(name="John Doe", email="john.doe@example.com")
    assert user.name == "John Doe"
    assert user.email == "john.doe@example.com"


def test_user_audit_model():
    audit = UserAudit(
        user_id=1, operation="create", previous_data={}, new_data={"name": "John Doe"}
    )
    assert audit.user_id == 1
    assert audit.operation == "create"
