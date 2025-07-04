from fastapi import FastAPI
from pydantic import BaseModel
from validators import validate_email, validate_phone, validate_password
from db import save_user_to_db, init_db
from models import Log
from database import SessionLocal

app = FastAPI()

class UserInput(BaseModel):
    email: str
    phone: str
    password: str

@app.get("/")
def read_root():
    return {"message": "Welcome to PK's FastAPI project!"}

@app.post("/register")
@validate_email
@validate_phone
@validate_password
async def register_user(user: UserInput):
    result = save_user_to_db(user)
    return result

@app.on_event("startup")
def startup_event():
    init_db()

from models import Log
from database import SessionLocal

@app.get("/logs")
def get_logs():
    session = SessionLocal()
    logs = session.query(Log).order_by(Log.timestamp.desc()).all()
    session.close()
    return [
        {
            "timestamp": log.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "level": log.level,
            "message": log.message
        }
        for log in logs
    ]