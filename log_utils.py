from database import SessionLocal
from models import Log

def log_to_db(log_type, level, message):
    session = SessionLocal()
    try:
        log_entry = Log(log_type=log_type, level=level, message=message)
        session.add(log_entry)
        session.commit()
    except Exception as e:
        print(f"[DB LOGGING FAILED] {e}")
        session.rollback()
    finally:
        session.close()
