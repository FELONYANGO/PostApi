from fastapi import FastAPI,Body,status,HTTPException,Response,APIRouter
from typing  import Optional
from pydantic import BaseModel
from passlib.context import CryptContext
import psycopg2
from psycopg2.extras import RealDictCursor
from . import main, schema, utils

router = APIRouter(
        prefix='/users',
        tags = ['Users']
)#routing the app defined in our hello.py file

# hashing the password
pwd_context= CryptContext(schemes=['bcrypt'],deprecated='auto')


@router.post('/')
def create_users(new_users:schema.Users):

         # hasht the password user.password
        
        new_users.password = utils.harsh(new_users.password)

        main.cur.execute(""" INSERT INTO users(email,password) VALUES (%s,%s) RETURNING * """,
                (new_users.email,new_users.password))
        
       
        post_users=main.cur.fetchone()

        main.con.commit(
             
        )
   
    
        return {"users": post_users}
# retreive users with id
@router.get('/{id}')
def  user_with_id(id = int):
        main.cur.execute("SELECT * FROM posts WHERE id= %s",(str(id)))
        conn= main.hello.cur.fetchone()
        if not conn:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post of id {id} not fount')

        return conn




