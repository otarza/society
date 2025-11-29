# 🎓 Junior Developer Learning Path

Welcome to the Girchi Digital Polis project! This guide is designed to take you from "I know some Python" to "I can build scalable backend systems."

This project uses a modern, professional technology stack. Don't be intimidated by the number of new terms—we will break them down one by one, using this project as our living textbook.

## 🗺️ Phase 1: The Big Picture (Business Logic)

Before writing code, we must understand *what* we are building.

### 📚 Concepts
- **Domain-Driven Design**: Writing code that matches real-world business concepts.
- **Data Modeling**: How we represent real-world entities (Users, Elections) in a computer.

### 🔍 Explore the Code
1. Read `initial.md` (The "Constitution" of our project).
2. Open `docs/data-model.md` and look at the diagram.
3. Open `app/models/user.py`. Notice how the `User` class matches the "User" concept in the documentation? That is **Data Modeling**.

### ✍️ Exercise 1: The Analyst
*Goal: Connect code to reality.*
1. Find the "Endorsement" concept in `initial.md`.
2. Find the corresponding table in `docs/data-model.md`.
3. Find the Python code in `app/models/endorsement.py`.
4. **Task**: Write a short paragraph explaining how the "Penalty" rule described in the text is represented in the database columns.

---

## 🐳 Phase 2: The Environment (Docker)

"It works on my machine" is the enemy. We use Docker to make sure it works everywhere.

### 📚 Concepts
- **Virtualization**: Creating a fake computer inside your computer.
- **Container**: A lightweight box that contains our app and everything it needs to run.
- **Docker Compose**: A tool to run multiple boxes (App, Database, Cache) together.

### 🔍 Explore the Code
1. Open `Dockerfile`. This is the recipe for building our App's box.
   - `FROM python:3.11-slim` -> Start with a basic Linux with Python installed.
   - `COPY . .` -> Copy our code into the box.
   - `RUN pip install...` -> Install libraries inside the box.
2. Open `docker-compose.yml`. This describes the orchestra.
   - See `services:`? It lists `db` (Postgres), `redis` (Cache), and `app` (Our code).

### ✍️ Exercise 2: The Operator
*Goal: Control the infrastructure.*
1. Run `docker-compose up -d`.
2. Run `docker ps` to see your running containers.
3. **Task**: "Kill" the database (`docker stop <db-container-id>`). Try to access the API. What happens?
4. Restart it (`docker start <db-container-id>`).

---

## 🐍 Phase 3: Modern Python (Type Hints & Pydantic)

We write "Strict Python" to catch bugs before they happen.

### 📚 Concepts
- **Type Hinting**: Telling Python "This variable must be an Integer".
- **Pydantic**: A library that enforces these rules automatically.

### 🔍 Explore the Code
1. Open `app/config.py`.
   - Look at `class Settings(BaseSettings)`.
   - See `POSTGRES_PORT: int = 5432`.
   - Try changing `5432` to `"hello"` in your `.env` file and run the app. It will crash immediately. **This is good!** It prevents bugs.

### ✍️ Exercise 3: The Enforcer
*Goal: Understand data validation.*
1. Create a new file `learning_pydantic.py`.
2. Define a Pydantic model for a `Car` (brand: str, year: int).
3. Try to create a Car with `year="two thousand"`. Watch it fail.
4. **Task**: Create a Pydantic schema for a "Pet" that requires a name, an age, and an optional breed.

---

## 🗄️ Phase 4: The Database (ORM & Migrations)

We don't write raw SQL queries (mostly). We use Python objects.

### 📚 Concepts
- **ORM (Object-Relational Mapper)**: A translator.
  - You speak Python: `user.name = "Giorgi"`
  - It speaks SQL: `UPDATE users SET name = 'Giorgi' ...`
- **Migrations (Alembic)**: Version control for your database structure. Like Git, but for tables.

### 🔍 Explore the Code
1. Open `app/models/territory.py`.
   - This is a Python class, but it creates a Database Table.
   - `mapped_column` defines a column.
   - `relationship` links it to other tables.
2. Look at `alembic/versions/`. These files track every change we make to the DB.

### ✍️ Exercise 4: The Architect
*Goal: Modify the database.*
1. We need to add a `nickname` field to the `User` model.
2. Open `app/models/user.py`.
3. Add: `nickname: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)`
4. Run: `docker-compose exec app alembic revision --autogenerate -m "Add nickname"`
5. Run: `docker-compose exec app alembic upgrade head`
6. Check the database (using Adminer at localhost:8080) to see your new column!

---

## ⚡ Phase 5: The API (FastAPI & Dependency Injection)

How the mobile app talks to our backend.

### 📚 Concepts
- **HTTP Methods**: GET (Read), POST (Create), PATCH (Update), DELETE.
- **Dependency Injection (DI)**: "Don't create tools, ask for them."
  - Instead of connecting to the DB inside every function, we say `db: AsyncSession = Depends(get_db)`. FastAPI hands us a ready-to-use connection.

### 🔍 Explore the Code
1. Open `app/api/v1/users.py`.
2. Look at `read_users_me`.
   - `current_user: User = Depends(get_current_user)`
   - We don't write code to check the token here. We just *ask* for the current user. FastAPI does the rest.

### ✍️ Exercise 5: The Builder
*Goal: Create an API endpoint.*
1. Open `app/api/v1/users.py`.
2. Create a new endpoint `GET /users/hello`.
3. It should take a query parameter `name`.
4. It should return `{"message": f"Hello {name}, welcome to Girchi!"}`.
5. Test it in the Swagger UI (localhost:8000/api/v1/docs).

---

## 🎓 Final Project: The "Mini-Feature"

Now combine everything.

**Task**: Implement a simple "Feedback" feature.
1. **Model**: Create a `Feedback` model (user_id, message, rating 1-5).
2. **Migration**: Create and run the migration.
3. **Schema**: Create a Pydantic schema for input validation.
4. **API**: Create an endpoint `POST /feedback` to save it.
5. **Test**: Use Swagger UI to send feedback and check the DB.

Good luck! We are building a society, one line of code at a time. 🚀
