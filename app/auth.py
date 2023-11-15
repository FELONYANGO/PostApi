from fastapi import Depends,APIRouter,Response,status,HTTPException
from . import schema,utils,main,auth2


router= APIRouter(  
    
   tags=['authentication']
)

@router.post('/login',response_model=schema.Token)
def login(user_details:schema.userloggins):
    user = main.cur.execute("""SELECT * FROM users WHERE email = %s""",(user_details.email,))
    conn = main.cur.fetchone()
   
    email= conn['email']
    passwords= conn['password']
    id=conn['id']
    
    if conn is None:
        # Add some logging to understand what's happening
        print(f"""Email: {email}""")
        print("No user found.")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='User does not exist')

    if not utils.verify_password(user_details.password, passwords):
        # Add some logging to understand what's happening
        print(f"Email: {user_details.email}, Password: {user_details.password}")
        print("Invalid credentials.")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentials')
    
    access_token=auth2.createToken(data={'id':id})

    return {"access_token": access_token, "token_type": "bearer token"}