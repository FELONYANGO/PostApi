from pydantic import BaseModel
from pydantic import EmailStr

class  Users(BaseModel):
    email: EmailStr
    password:str


