from fastapi import Depends,APIRouter,Response,status,HTTPException
from . import schema,utils,main


router= APIRouter(  
   tags=['authentication']
)

@router.post('/login')
def login(user_details:schema.userloggins):
    user = main.cur.execute('SELECT * FROM users WHERE email = %s ',(user_details.email))
    conn = main.cur.fetchone()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user does not exist')

    if not utils.verify_password(user_details.password,user.password):

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f'invalid credentials')
    
