from fastapi import FastAPI,Body,status,HTTPException,Response
from typing  import Optional
from pydantic import BaseModel

import psycopg2
from psycopg2.extras import RealDictCursor
from . import posts,users,auth



# 

# code for hashing user password in the database


app = FastAPI()


   
# connect to the database

try  :     
     con= psycopg2.connect(
                host='localhost',
                dbname ='postgres',
                user='postgres',
                password='6200felix',
            
                cursor_factory=RealDictCursor
                )
     cur = con.cursor()
     
     print('connection succefully established')
except Exception as error:
            print('connection failed')
            print(error)


# since our code right now only save our data into the  memory,,we want to store it into an array
my_posts=[]

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

# the  root view function

@app.get('/')
def root():
    return {'root':'this is the root home page'}






# function to get specific id
def get_id(id):
    for ids in my_posts:
        if ids['id'] == id:
            return ids

    





# function to update user



# getting id of post
def get_id_post(id):
     for i, d in enumerate(my_posts) :
        if d['id'] == id:
            return i


     
    

# @app.put('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
# def update_post(id: int,post:Post):
     
#        indexs = get_id_post(id)
     
#        if indexs == None:
       
#             raise HTTPException( status.HTTP_204_NO_CONTENT,detail=f'post with {id} does not exist')
    
#        post_dict = post.model_dump()  
#        post_dict['id'] = id
#        post_dict = my_posts[indexs] 
#        print(type(post_dict))
#        return post_dict


