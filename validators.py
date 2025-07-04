import re
from fastapi.responses import JSONResponse
from functools import wraps
from log_utils import log_to_db

def validate_email(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        user = kwargs.get("user")
        if not user:
            log_to_db("validation", "WARNING", "Missing user data during email validation.")
            return JSONResponse(status_code=400, content={"error": "Missing user data"})
        if not re.match(r"[^@]+@[^@]+\.[^@]+", user.email):
            log_to_db("validation", "WARNING", f"Invalid email format attempted: {user.email}")
            return JSONResponse(status_code=400, content={"error": "Invalid email format"})
        return await func(*args, **kwargs)
    return wrapper

def validate_phone(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        user = kwargs.get("user")
        if not user:
            log_to_db("validation", "WARNING", "Missing user data during phone validation.")
            return JSONResponse(status_code=400, content={"error": "Missing user data"})
        if not user.phone.isdigit() or len(user.phone) != 10:
            log_to_db("validation", "WARNING", f"Phone validation failed for email={user.email}, phone={user.phone}")
            return JSONResponse(status_code=400, content={"error": "Phone must be exactly 10 digits"})
        return await func(*args, **kwargs)
    return wrapper

def validate_password(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        user = kwargs.get("user")
        if not user:
            log_to_db("validation", "WARNING", "Missing user data during password validation.")
            return JSONResponse(status_code=400, content={"error": "Missing user data"})
        if (
            len(user.password) < 8
            or not re.search(r"[A-Z]", user.password)
            or not re.search(r"\d", user.password)
        ):
            masked_pwd = f"{user.password[:4]}****"
            log_to_db("validation", "WARNING", f"Password validation failed for email={user.email}, password={masked_pwd}")
            return JSONResponse(
                status_code=400,
                content={"error": "Password must be at least 8 characters long, include one uppercase letter and one number"}
            )
        return await func(*args, **kwargs)
    return wrapper
