from . import  main
from fastapi import FastAPI,Body,status,HTTPException,Response,APIRouter
from passlib.context import CryptContext
import psycopg2
from psycopg2.extras import RealDictCursor
from . import schema

router = APIRouter(
    prefix='/posts',
    tags= ['Posts']
)

# the function to retrieve posts
@router.get('/')
def get_posts():
    main.cur.execute('SELECT * FROM posts')
    res= main.cur.fetchall()
   
    return res

# fonction to create posts
@router.post('/')
def create_post(new_post:schema.Post):
    main.cur.execute(""" INSERT INTO posts(title,content,published) VALUES (%s,%s,%s) RETURNING * """,
               (new_post.title,new_post.content,new_post.published))
    post_content=main.cur.fetchone()
    main.con.commit()
    return {"posts": post_content}


# the function to retrieve single post
@router.get('/{id}')
def get_post(id:int):
    main.cur.execute("SELECT * FROM posts WHERE id= %s",(str(id)))
    conn= main.cur.fetchone()
    if not conn:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post of id {id} not fount')

    return conn



# updating a single user using id
@router.put('/{id}')
def update_post(id: int,post:schema.Post):
        main.cur.execute(""" UPDATE posts SET title=%s, content=%s,published=%s WHERE id=%s  RETURNING *""",
                   (post.title,post.content,post.published,str(id)))
        updated_post=main.cur.fetchone()
        print(updated_post)
        main.con.commit()
       
        if updated_post == None :
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                 detail=f'the with id{id} post was not found')
     
        return {'message': updated_post}

# function to delete post
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    main.cur.execute('DELETE  FROM posts WHERE id=%s returning *',(str(id)))
    indexs = main.cur.fetchone()
    main.con.commit()
    if indexs==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'pst with id {id} does not exist')
    
    return Response(status_code=status.HTTP_200_OK)
    


