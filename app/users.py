from fastapi import FastAPI,Body,status,HTTPException,Response,APIRouter
from typing  import Optional
from pydantic import BaseModel
from passlib.context import CryptContext
import psycopg2
from psycopg2.extras import RealDictCursor
from . import schema,hello

router = APIRouter(
        prefix='/users'
)#routing the app defined in our hello.py file

# hashing the password
pwd_context= CryptContext(schemes=['bcrypt'],deprecated='auto')


router.post('/')
def create_users(new_users:schema.Users):

         # hasht the password user.password
        hashed_pwd = pwd_context.hash(new_users.password)
        new_users.password = hashed_pwd

        hello.cur.execute(""" INSERT INTO users(email,password) VALUES (%s,%s) RETURNING * """,
                (new_users.email,new_users.password))
        
       
        post_users=hello.cur.fetchone()

        hello.con.commit(
             
        )
   
    
        return {"users": post_users}
