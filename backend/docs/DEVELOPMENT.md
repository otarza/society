# Development Setup Guide

## Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Git

## Local Environment Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd society/backend
   ```

2. **Create environment file**
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   Update the `.env` file with your configuration if needed.

3. **Start services with Docker Compose**
   This will start PostgreSQL, Redis, and the FastAPI application in development mode.
   ```bash
   docker-compose up -d
   ```

4. **Run Database Migrations**
   Initialize the database schema:
   ```bash
   docker-compose exec app alembic upgrade head
   ```

5. **Access the Application**
   - API Documentation (Swagger UI): http://localhost:8000/api/v1/docs
   - ReDoc: http://localhost:8000/api/v1/redoc
   - Adminer (Database UI): http://localhost:8080 (System: PostgreSQL, Server: db, Username: postgres, Password: postgres, Database: society_db)

## Development Workflow

### Running Tests
To run the test suite:
```bash
docker-compose exec app pytest
```

### Creating Migrations
When you modify models in `app/models/`, create a new migration:
```bash
docker-compose exec app alembic revision --autogenerate -m "description of changes"
```
Then apply it:
```bash
docker-compose exec app alembic upgrade head
```

### Code Style
The project uses `black` for formatting and `ruff` for linting.
```bash
docker-compose exec app black .
docker-compose exec app ruff check .
```

## Project Structure

- `app/api`: API route handlers
- `app/core`: Core configuration and utilities
- `app/models`: SQLAlchemy database models
- `app/schemas`: Pydantic schemas for validation
- `app/services`: Business logic layer
- `alembic`: Database migration scripts
- `tests`: Test suite

## Troubleshooting

### Database Connection Issues
If the app cannot connect to the database, ensure the `db` service is healthy:
```bash
docker-compose ps
docker-compose logs db
```

### Resetting the Database
To completely reset the database (WARNING: deletes all data):
```bash
docker-compose down -v
docker-compose up -d
docker-compose exec app alembic upgrade head
```
