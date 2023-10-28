from fastapi import FastAPI,Body,status,HTTPException,Response
from typing  import Optional
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from . import schema


# 



app = FastAPI()

# creating the post schema
class Post(BaseModel):
    title: str
    content: str
    published :Optional[bool]
   
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


# the  root view function
@app.get('/')
def root():
    return {'root':'this is the root home page'}

# the function to retrieve posts
@app.get('/posts/')
def get_posts():
    cur.execute('SELECT * FROM posts')
    res= cur.fetchall()
   
    return res


# fonction to create posts
@app.post('/posts')
def create_post(new_post:Post):
    cur.execute(""" INSERT INTO posts(title,content,published) VALUES (%s,%s,%s) RETURNING * """,
               (new_post.title,new_post.content,new_post.published))
    post_content=cur.fetchone()
    con.commit()
    return {"posts": post_content}


# function to get specific id
def get_id(id):
    for ids in my_posts:
        if ids['id'] == id:
            return ids

    

# the function to retrieve single post
@app.get('/posts/{id}')
def get_post(id:int):
    cur.execute("SELECT * FROM posts WHERE id= %s",(str(id)))
    conn= cur.fetchone()
    if not conn:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post of id {id} not fount')

    return conn



# function to update user



# getting id of post
def get_id_post(id):
     for i, d in enumerate(my_posts) :
        if d['id'] == id:
            return i


@app.put('/posts/{id}')
def update_post(id: int,post:Post):
        cur.execute(""" UPDATE posts SET title=%s, content=%s,published=%s WHERE id=%s  RETURNING *""",
                   (post.title,post.content,post.published,str(id)))
        updated_post=cur.fetchone()
        print(updated_post)
        con.commit()
       
        if updated_post == None :
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                 detail=f'the with id{id} post was not found')
     
        return {'message': updated_post}



# function to delete post
@app.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cur.execute('DELETE  FROM posts WHERE id=%s returning *',(str(id)))
    indexs = cur.fetchone()
    con.commit()
    if indexs==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'pst with id {id} does not exist')
    
    return Response(status_code=status.HTTP_200_OK)
    
        
    

@app.put('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
def update_post(id: int,post:Post):
     
       indexs = get_id_post(id)
     
       if indexs == None:
       
            raise HTTPException( status.HTTP_204_NO_CONTENT,detail=f'post with {id} does not exist')
    
       post_dict = post.model_dump()  
       post_dict['id'] = id
       post_dict = my_posts[indexs] 
       print(type(post_dict))
       return post_dict


@app.post('/users')
def create_users(new_users:schema.Users):

     
        cur.execute(""" INSERT INTO users(email,password) VALUES (%s,%s) RETURNING * """,
                (new_users.email,new_users.password))
        if not schema.email:
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                 detail=f'the with id{id} post was not found')
       
        post_users=cur.fetchone()

        con.commit(
             
        )
   
    
        return {"users": post_users}

