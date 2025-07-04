from models import User
from database import SessionLocal, Base, engine
from log_utils import log_to_db

def save_user_to_db(user_data):
    session = SessionLocal()
    try:
        log_to_db("db", "INFO", f"Attempting to save user: {user_data.email}")
        user = User(
            email=user_data.email,
            phone=user_data.phone,
            password=user_data.password
        )
        session.add(user)
        session.commit()
        log_to_db("db", "INFO", f"User {user_data.email} saved successfully with id {user.id}.")
        return {"status": "success", "user_id": user.id}
    except Exception as e:
        session.rollback()
        if 'duplicate key value' in str(e):
            log_to_db("db", "WARNING", f"Duplicate email registration attempt: {user_data.email}")
            return {"status": "error", "message": "Email already exists"}
        log_to_db("db", "ERROR", f"Error saving user: {str(e)}")
        return {"status": "error", "message": "Internal Server Error"}
    finally:
        session.close()

def init_db():
    Base.metadata.create_all(bind=engine)