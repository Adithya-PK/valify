from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    log_type = Column(String, nullable=False)  # 'db' or 'validation'
    level = Column(String, nullable=False)     # INFO / WARNING / ERROR
    message = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)