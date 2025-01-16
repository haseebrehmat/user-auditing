"""
CRUD operations for database interaction.
"""

from sqlalchemy.orm import Session
from app.models import User, UserAudit


def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    log_audit(db, user.id, "create", None, {"name": name, "email": email})
    return user


def log_audit(
    db: Session, user_id: int, operation: str, previous_data: dict, new_data: dict
):
    audit_entry = UserAudit(
        user_id=user_id,
        operation=operation,
        previous_data=previous_data,
        new_data=new_data,
    )
    db.add(audit_entry)
    db.commit()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_all_users(db: Session):
    return db.query(User).all()


def update_user(db: Session, user_id: int, name: str, email: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    previous_data = {"name": user.name, "email": user.email}
    user.name = name
    user.email = email
    db.commit()
    db.refresh(user)

    log_audit(db, user_id, "update", previous_data, {"name": name, "email": email})
    return user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    previous_data = {"name": user.name, "email": user.email}
    db.delete(user)
    db.commit()

    log_audit(db, user_id, "delete", previous_data, None)
    return user
