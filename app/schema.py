from pydantic import BaseModel
from pydantic import EmailStr
from typing import Optional


class Post(BaseModel):
    title:str
    content:str
    published:bool = True
# User login credentials
class  Users(BaseModel):
    email: EmailStr
    password:str

    
class userloggins(BaseModel):
    email:EmailStr
    password:str

# User server response on login.for te dev environment only
class Usersout(BaseModel):
    id:int
    email:EmailStr

# token format retarned when user create a token
class Token(BaseModel):
    access_token:str
    token_type:str

# token data when decoded duri
class TokenData(BaseModel):
    id:Optional[int]




