"""
Tests for CRUD operations.
"""

from app.crud import (
    create_user,
    get_user_by_id
)
from sqlalchemy.orm import Session


def test_create_user_crud(db_session: Session):
    user = create_user(db_session, name="Jane Doe", email="jane.doe@example.com")
    assert user.name == "Jane Doe"
    assert user.email == "jane.doe@example.com"


def test_get_user_by_id_crud(db_session: Session):
    user = get_user_by_id(db_session, user_id=1)
    assert user is not None
