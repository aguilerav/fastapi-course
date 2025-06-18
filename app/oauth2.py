import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta

# SECRET KEY
# Algorithm
# Expiration time

SECRET_KEY = "ad7065e10a5c4331b7114f2b1d303b219a3ce8bf83dd20855909695e9e13a9aa"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
