from fastapi import APIRouter, status, Depends, HTTPException
from src.schemas.schemas import User, UserSimple, LoginData, LoginSuccessSchema
from src.base.sqlalchemy.config.db import get_db
from src.base.sqlalchemy.repositorys.user import UserRepository
from sqlalchemy.orm import Session
from src.base.providers import hash_provider, token_provider
from src.routes.auth_utils import get_user_logged

router = APIRouter()


@router.post('/token', response_model=LoginSuccessSchema)
def login(logindata: LoginData, session: Session = Depends(get_db)):

    user = UserRepository(session).searchByEmailValid(logindata.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Não existe nenhum cadastro de usuário com esse email.")

    password_valid = hash_provider.hash_verify(
        logindata.password, user.password)
    if not password_valid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="A senha está incorreta")
    # Gerar token JWT
    token = token_provider.create_acess_token({'sub': user.email})

    return LoginSuccessSchema(user=user, access_token=token)


@router.get('/profile', response_model=UserSimple)
def profile(user: User = Depends(get_user_logged), session: Session = Depends(get_db)):
    return user


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserSimple)
async def signup(user: User, session: Session = Depends(get_db)):

    userVerifyEmail = UserRepository(session).searchByEmail(user.email)
    if userVerifyEmail:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email ja cadastrado. Faça o login ou cadastre outro email")

    userVerifyCPF = UserRepository(session).searchByCPF(user.cpf)
    if userVerifyCPF:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="CPF ja cadastrado. Digite o CPF correto e tente novamente")

    user.password = hash_provider.hash_generate(user.password)
    userCreated = UserRepository(session).create(user)
    return userCreated


@router.get('/me')
def me(user: User = Depends(get_user_logged)):
    return user
