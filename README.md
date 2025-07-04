# 🚀 FastAPI Registration API

A simple FastAPI project with custom input validation (email, phone, password), PostgreSQL integration, and database-stored logs.

## ⚙ Tech Stack

- FastAPI
- Pydantic
- PostgreSQL
- SQLAlchemy
- Decorators for validation
- Logs stored directly in a logs table

## 🛠 Setup Instructions

1. *Clone the repo and enter the folder*
2. *Create and activate virtual environment*
3. *Install dependencies*
4. *Create a PostgreSQL database*  
      - Make sure this matches the connection string in database.py:
        DATABASE_URL = "postgresql://postgres:root@localhost/fastapi_db"
5. *Run the application*
      - uvicorn main:app --reload

## 🧪 Test the API

1. Open your browser and go to:
      - http://127.0.0.1:8000/docs
2. Click on /register → *Try it out* → Enter sample data:
3. Click Execute — if all inputs are valid, it will be saved to the database.

## 🔎 How to Check Data

1. Users Table:
      - SELECT * FROM users;

3. Validation & DB Logs Table:
      - SELECT * FROM logs;


## 🧾 File Structure (Quick Guide)

- main.py – App startup, route definitions, request model, and usage of custom validation decorators.
- validators.py – Contains custom decorators to validate email, phone, and password input using regex, with logging.
- db.py – Handles saving user data and validation logs into the PostgreSQL database using SQLAlchemy.
- models.py – Defines SQLAlchemy ORM models for the users and logs tables.
- database.py – Initializes the database engine, session factory, and base class for ORM models.
- logger.py – (Now optional) Previously used for file-based logging; replaced with database logging logic.
- log_utils.py – Contains logic to save validation logs into the database instead of writing to log files.
- requirements.txt – Lists all the dependencies needed to install and run the project (e.g., FastAPI, SQLAlchemy, psycopg2).
