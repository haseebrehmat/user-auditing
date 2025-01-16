# Implementation Plan

## Overview
This document outlines the implementation plan for the **User Profile Audit Challenge**, including design choices, implementation steps, and additional features/optimizations.

---

## Implementation Steps

### 1. Environment Setup
- **Tools & Libraries**:
  - Python 3.10+
  - FastAPI
  - PostgreSQL
  - SQLAlchemy/`asyncpg`
  - `pytest`
- **Setup Steps**:
  1. Initialize a FastAPI project.
  2. Install required libraries using `pip`:
  3. Create a PostgreSQL database.
  4. Set up environment variables using `.env` (e.g., database URL, port).

### 2. Database Design
- **Schema**:
  - **users** (Active profiles):
    ```sql
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ```
  - **user_audit** (Change log):
    ```sql
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    operation VARCHAR(50),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    previous_data JSONB,
    new_data JSONB
    ```

### 3. API Endpoints

#### **User CRUD Operations**
- **POST /users**: Create a new user.
- **GET /users**: Retrieve all users.
- **GET /users/{id}**: Retrieve a specific user by ID.
- **PUT /users/{id}**: Update user details and log the change in `user_audit`.
- **DELETE /users/{id}**: Soft delete a user and log the change.

#### **Audit Endpoint**
- **GET /audit**: Retrieve a full audit log, including all changes with timestamps.

### 4. Logging Changes
- On updates and deletions, the old data will be logged in the `user_audit` table with the operation type (`update`, `delete`).
- Example Audit Entry:
  ```json
  {
    "user_id": 1,
    "operation": "update",
    "timestamp": "2025-01-14T12:00:00Z",
    "previous_data": { "name": "John Doe", "email": "john.doe@example.com" },
    "new_data": { "name": "John Smith", "email": "john.smith@example.com" }
  }
  ```

### 5. Validation & Error Handling
- **Validations**:
  - Unique email constraint.
  - Name and email format checks using Pydantic.
- **Error Handling**:
  - Return proper HTTP status codes (e.g., `400` for bad requests, `404` for not found).
  - Include detailed error messages in JSON responses.

### 6. Testing
- Write unit and integration tests using `pytest`:
  - Test each endpoint for success and failure scenarios.
  - Mock database operations using fixtures.

### 7. Docker Integration
- Create a `Dockerfile`
- Add `docker-compose.yml`


## Additional Notes

### Architectural Choices
- **Layered Architecture**: Keeps the codebase modular and maintainable.
  - **Router Layer**: FastAPI routes.
  - **Service Layer**: Business logic.
- **Audit Logging**: Ensures all changes are captured without data loss.
- **Soft Deletes**: Prevents accidental data loss while maintaining data integrity.



# Additional Features & Optimizations
1. **Pagination for Logs**:
   - Enable pagination in the `/audit` endpoint to handle large datasets.
2. **Search & Filters**:
   - Add query parameters to filter logs by user, operation type, or date range.
3. **Optimized Indexing**:
   - Index frequently queried columns like `user_id` and `timestamp` in the `user_audit` table.
4. **Asynchronous Database Operations**:
   - Use `asyncpg` for non-blocking database queries.
5. **API Documentation**:
   - Utilize FastAPI's auto-generated Swagger UI (`/docs`) for clear API documentation.
6. **Scalability**:
   - Configure connection pooling for PostgreSQL using `asyncpg`.
7. **Monitoring**:
   - Add logging and error monitoring with tools like Sentry.


