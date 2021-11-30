from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    country: str
    state: str
    city: str
    zipcode: str
    street: str
    number: str
    complement: str
    cpf: str
    pis: str
    password: str

    class Config:
        orm_mode = True

class UserNoPassword(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    country: str
    state: str
    city: str
    zipcode: str
    street: str
    number: str
    complement: str
    cpf: str
    pis: str
class UserSimple(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    cpf: str
    class Config:
        orm_mode = True

class LoginData(BaseModel):
    email: str
    password: str

class LoginSuccessSchema(BaseModel):
    user: UserSimple    
    access_token: str