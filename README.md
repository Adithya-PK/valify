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

Users Table:
      - SELECT * FROM users;

Validation & DB Logs Table:
      - SELECT * FROM logs;


## 🧾 File Structure (Quick Guide)

main.py -	App startup, routing, and decorators usage
validators.py	- Custom email, phone, and password checks
db.py	- Save users and log to DB
models.py	- SQLAlchemy models for User and Log
database.py	- PostgreSQL connection setup
requirements.txt - Project dependencies

---
