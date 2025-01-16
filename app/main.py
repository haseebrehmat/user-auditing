"""
Main application entry point.
"""

from fastapi import FastAPI
from app.db.connection import engine
from app.db.migration import run_migrations
from app.routes import user_routes, audit_routes

# Initialize database
run_migrations(engine)

# Initialize the app
app = FastAPI()

# Include routes
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(audit_routes.router, prefix="/audit", tags=["Audit"])
