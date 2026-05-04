from datetime import datetime, timedelta
from jose import jwt
from fastapi import HTTPException

# Note: Install python-jose with: pip install python-jose[cryptography]

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


def create_token(username: str):

    payload = {
        "sub": username,
        "exp": datetime.utcnow()
        + timedelta(hours=2)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token