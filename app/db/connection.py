"""Database connection, session management, and database readiness check."""

import os
import time
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database URL construction
DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}"
    f"@{os.getenv('DATABASE_HOST', 'db')}:{os.getenv('DATABASE_PORT', '5432')}/{os.getenv('DATABASE_NAME')}"
)


def wait_for_db(max_retries=60, retry_interval=1):
    temp_engine = create_engine(DATABASE_URL)

    for attempt in range(max_retries):
        try:
            # Try to connect and execute a simple query
            with temp_engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            print("Database is ready!")
            temp_engine.dispose()
            return True
        except OperationalError as e:
            if attempt < max_retries - 1:
                print(f"Waiting for database... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(retry_interval)
            else:
                print("Max retries reached. Database is not available.")
                raise e


# Create engine after ensuring database is available
if __name__ == "__main__":
    wait_for_db()
else:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
