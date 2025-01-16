"""
Database migrations (create tables).
"""
from sqlalchemy import Engine
from app.models import Base

def run_migrations(engine: Engine):
    Base.metadata.create_all(bind=engine)