from pydantic import BaseModel
from pydantic import EmailStr
from typing import Optional


# creating the post schema
class Post(BaseModel):
    title: str
    content: str
    published :Optional[bool]


class  Users(BaseModel):
    email: EmailStr
    password:str


class Usersout(BaseModel):
    id:int
    email:EmailStr


class userloggins(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    token:str
    tokentype:str

class TokenData(BaseModel):
    id:Optional[str]




