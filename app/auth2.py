from jose import JWTError,jwt
from datetime import datetime,timedelta

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# method for creating the authentication token
def createToken(data:dict):
    to_encode=data.copy()

    expiry = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'expires': expiry.isoformat()})  

    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return token
