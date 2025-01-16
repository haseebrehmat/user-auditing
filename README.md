# 📖 User Auditing

This project is a FastAPI-based application for managing user profiles with a full audit log. It ensures that all changes to user profiles are logged for auditing purposes, even when users are updated or deleted. The application integrates PostgreSQL for data persistence and is containerized using Docker.

---

## 🛠️ Built With

- **[FastAPI](https://fastapi.tiangolo.com/):** A modern, fast web framework for Python.
- **[PostgreSQL](https://www.postgresql.org/):** Robust relational database for data storage.
- **[SQLAlchemy](https://www.sqlalchemy.org/):** ORM for database operations.
- **[Docker](https://www.docker.com/):** For containerization and deployment.
- **[Pytest](https://pytest.org/):** For automated testing.

---

## 🚀 Getting Started

### Prerequisites

1. Install **Docker** and **Docker Compose**:
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)
   - [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

2. Clone the repository:
   ```bash
   git clone git@github.com:haseebrehmat/user-auditing.git
   cd user-auditing
   ```

---

## 📦 Installation

1. Copy the example `.env` file and update the necessary credentials:
   ```bash
   cp .env.example .env
   ```

2. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

---

## ⚙️ Usage

### API Endpoints

#### User Management
| Method | Endpoint          | Description                     |
|--------|-------------------|---------------------------------|
| POST   | `/users/`         | Create a new user profile       |
| GET    | `/users/`         | List all user profiles          |
| GET    | `/users/{user_id}`| Retrieve a specific user profile|
| PUT    | `/users/{user_id}`| Update a user profile           |
| DELETE | `/users/{user_id}`| Delete a user profile           |

#### Audit Logs
| Method | Endpoint | Description                         |
|--------|----------|-------------------------------------|
| GET    | `/audit` | Retrieve the full audit log         |

### Testing

1. Run tests using `pytest`:
   ```bash
   docker-compose exec app pytest
   ```

---

## 🛤️ Roadmap

## 🗂️ Code Information

### Application Files

- **`app/main.py`**: Entry point of the application; initializes routes, database, and FastAPI.
- **`app/models.py`**: Defines the database models (`User` and `UserAudit`).
- **`app/schemas.py`**: Pydantic schemas for data validation and serialization.
- **`app/database/connection.py`**: Manages database connection and session handling.
- **`app/database/migrations.py`**: Handles database migrations (e.g., creating tables).
- **`app/database/seeders.py`**: Populates the database with initial seed data.
- **`app/crud.py`**: Contains CRUD operations for interacting with the database.
- **`app/services/audit_service.py`**: Business logic for fetching audit logs.
- **`app/routes`**:
  - `user_routes.py`: Handles API endpoints for user-related operations.
  - `audit_routes.py`: Handles API endpoints for audit logs.

### Test Files

- **`tests/test_models.py`**: Unit tests for database models.
- **`tests/test_schemas.py`**: Tests for Pydantic schemas to ensure data validation.
- **`tests/test_crud.py`**: Tests for CRUD operations to validate database interactions.
- **`tests/test_routes.py`**: Integration tests for API routes.
- **`tests/test_services.py`**: Tests for service logic (e.g., audit log fetching).

---

## 📝 Improvements and Future Work


- [x] CRUD operations for users.
- [x] Full audit logging.
- [x] Dockerized deployment.
- [x] API testing with Pytest.
- [ ] Add advanced search/filtering for audit logs.
- [ ] Add pagination for audit logs & users.
- [ ] Implement authentication and authorization.
- [ ] Enhance error handling with custom middlewares.

---

Feel free to contribute or provide feedback! 🚀

