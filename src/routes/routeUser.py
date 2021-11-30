from fastapi import APIRouter, status, Depends, HTTPException
from src.schemas.schemas import User, UserSimple, LoginData, LoginSuccessSchema, UserNoPassword
from src.base.sqlalchemy.config.db import get_db
from src.base.sqlalchemy.repositorys.user import UserRepository
from sqlalchemy.orm import Session
from src.base.providers import hash_provider, token_provider
from src.routes.auth_utils import get_user_logged

router = APIRouter()


@router.get('/users', status_code=status.HTTP_200_OK, response_model=UserNoPassword)
async def index(session: Session = Depends(get_db), user: User = Depends(get_user_logged)):
    user_list = UserRepository(session).list()
    return user_list


@router.get("/users/{id}", status_code=status.HTTP_200_OK, response_model=UserNoPassword)
def show_user(id: int, session: Session = Depends(get_db), user: User = Depends(get_user_logged)):
    userFound = UserRepository(session).searchById(id)
    if not userFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Usuário não encontrado')
    return userFound


@router.put('/users/{id}')
async def update(id: int, user: User, session: Session = Depends(get_db), userAuth: User = Depends(get_user_logged)):
    userSearch = UserRepository(session).getUser(id)

    if(user.password is None):
        user.password = userSearch.password
    else:
        user.password = hash_provider.hash_generate(user.password)
    return UserRepository(session).edit(id, user)


@router.delete('/users/{id}')
def delete_user(id: int, session: Session = Depends(get_db)):
    UserRepository(session).delete(id)
    return
