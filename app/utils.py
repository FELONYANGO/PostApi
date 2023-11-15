from passlib.context import CryptContext

pwd_context= CryptContext(schemes=['bcrypt'],deprecated='auto')

"""
this function handles the logic of the password  harshing
"""

def harsh (password : str):
    return pwd_context.hash(password)


"""
takes the password passed during user loggin,compares it with the one
exixting in the db 

"""
def verify_password(plain_pswd,hashed_pswd):
    return pwd_context.verify(plain_pswd,hashed_pswd)
