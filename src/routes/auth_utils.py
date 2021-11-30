from fastapi import Depends, HTTPException, status
from src.base.sqlalchemy.config.db import get_db
from fastapi.security import OAuth2PasswordBearer
from src.base.sqlalchemy.repositorys.user import UserRepository
from sqlalchemy.orm import Session
from src.base.providers import token_provider
from jose import JWTError

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def get_user_logged(token:str =  Depends(oauth2_schema), session: Session = Depends(get_db)):

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token Inválido')

    try:
        email = token_provider.verify_acess_token(token)
    except JWTError:
        raise exception
    
    if not email:
        raise exception

    user = UserRepository(session).searchByEmail(email)

    if not user:
        raise exception

    return user