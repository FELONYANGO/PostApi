from passlib.context import CryptContext

pwd_context= CryptContext(schemes=['bcrypt'],deprecated='auto')
"""
the  functions passed in this file handles the logic of the password  harshing"""

def harsh (password : str):
    return pwd_context.hash(password)


"""
hash the password that is taken form the user during the logging
the password is used to create   jwt tokens for authosization on the api usge

"""
def verify_password(plain_pswd,hashed_pswd):
    return pwd_context.verify(plain_pswd,hashed_pswd)
