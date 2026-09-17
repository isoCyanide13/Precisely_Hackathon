# FastAPI Modular Backend

A scalable, production-grade FastAPI application built with SQLAlchemy 2.0, Alembic migrations, and JWT authentication.

---

## 📁 Directory Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                  # App initialization, CORS, routing, lifespan
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py              # Auth & DB session dependency injection
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py           # V1 route aggregator
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           ├── auth.py      # /login, /login/access-token, /register, /me
│   │           ├── users.py     # User management CRUD
│   │           └── health.py    # Service health status
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py            # Pydantic v2 settings (.env loading)
│   │   └── security.py          # Password hashing (bcrypt) & JWT helpers
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base_class.py        # SQLAlchemy DeclarativeBase with mixins
│   │   ├── base.py              # Model imports for Alembic migrations
│   │   └── session.py           # Engine & SessionLocal setup
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py              # User database model
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── token.py             # Token & TokenPayload schemas
│   │   └── user.py              # User schemas (Create, Read, Update)
│   └── services/
│       ├── __init__.py
│       └── user_service.py      # User business logic and DB queries
├── alembic/                     # Database migrations
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── alembic.ini                  # Alembic configuration
├── .env.example                 # Example environment variables
├── .env                         # Local environment variables
├── .gitignore                   # Ignored files
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 🚀 Quickstart

### 1. Activate the Conda Environment

The Conda virtual environment has been created under `backend/.venv`.

**Using Conda (PowerShell / Command Prompt / Terminal):**
```powershell
cd backend
conda activate .\ .venv
# or using the full path:
conda activate D:\Precisely_Hackathon\backend\.venv
```

**Directly with the Scripts folder (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment

Copy `.env.example` to `.env` if not already created:
```bash
cp .env.example .env
```

*By default, `DATABASE_URL` is set to `sqlite:///./sql_app.db` for zero-friction local development.*
*To use PostgreSQL, update `DATABASE_URL` in `.env` to:*
```env
DATABASE_URL="postgresql+psycopg2://<user>:<password>@localhost:5432/<db_name>"
```

---

### 4. Run Migrations (Optional)

Tables are automatically created upon startup for quick development, but you can also use Alembic for versioned schema migrations:

```bash
# Generate a new migration
alembic revision --autogenerate -m "create user table"

# Apply migrations
alembic upgrade head
```

---

### 5. Start the FastAPI Development Server

```bash
uvicorn app.main:app --reload --port 8000
```

---

## 📚 Interactive API Documentation

Once the server is running, visit:
- **Swagger UI**: [http://localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs)
- **ReDoc**: [http://localhost:8000/api/v1/redoc](http://localhost:8000/api/v1/redoc)
- **Health Check**: [http://localhost:8000/api/v1/health](http://localhost:8000/api/v1/health)

---

## 🔑 Key Features

- **Layered Architecture**: Clear separation of concerns (`api` -> `services` -> `db/models`).
- **Pydantic v2 Settings**: Strongly typed environment configurations with validation.
- **SQLAlchemy 2.0**: Modern typed ORM patterns with `mapped_column` and `Mapped`.
- **JWT Authentication**: Secure Bearer tokens with configurable expiration and bcrypt password hashing.
- **CORS Configured**: Pre-configured for React/Vite development on `http://localhost:5173`.
