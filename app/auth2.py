from jose import JWTError,jwt
from datetime import datetime,timedelta
from . import schema
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer


# to get a string like this run:
# openssl rand -hex 32

oath2_scheme = OAuth2PasswordBearer(tokenUrl='login')


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


def veryfylogin(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:str=  payload.get("id")

        if id is None:
            raise credentials_exception
        
        token_data = schema.TokenData(id=id)

    except JWTError:
        raise credentials_exception
    
    return token_data

# getting the current user
def get_current_user(token:str=Depends(oath2_scheme)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail= f"could not validate the  user credentials",headers={'www-authentication':'bearer'})


    return veryfylogin(token,credentials_exception)