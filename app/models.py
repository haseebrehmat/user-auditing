"""
Database models.
"""

from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)


class UserAudit(Base):
    __tablename__ = "user_audit"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    operation = Column(String, nullable=False)  # "create", "update", "delete"
    timestamp = Column(DateTime, server_default=func.now())
    previous_data = Column(JSON, nullable=True)
    new_data = Column(JSON, nullable=True)
