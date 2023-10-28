from pydantic import BaseModel
from pydantic import EmailStr

class  Users(BaseModel):
    email: EmailStr
    password:str


class Usersout(BaseModel):
    id:int
    email:EmailStr

