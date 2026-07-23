# used to encrypt the password / compare the passwords
import bcrypt

# used to generate tokens (jwt) 
import jwt

# set exp date to tokens
from datetime import datetime,timedelta,timezone

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
import models
from database import get_db



# used to convert readable data to unreadable format
SECRET_KEY = "1c985c23f8be6b316464c92b07f246d6e5aeb59577388be43b9ba104e3cd703e"
ALGORITHM = "HS256"

# Expire time to token
ACCESS_TOKEN_EXPIRE_MINUTES = 30


security = HTTPBearer() #reads "Authorization : Bearer <token>" header

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

    except jwt.ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail= "TOKEN EXPIRED")
    except jwt.InvalidTokenError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail= "INVALID TOKEN")
    
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail= "User not Found!!!!")
    return user

          

# Generate Hashed Password
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()


# Compare the passwords
def verify_password(plain:str,hashed:str)->bool:
    return bcrypt.checkpw(plain.encode(),hashed.encode())

# create token
def create_access_token(username: str) -> str:
    payload = {
        "sub": username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

