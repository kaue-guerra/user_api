from sqlalchemy import Column, Integer, String, Boolean
from src.base.sqlalchemy.config.db import Base

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    country = Column(String)
    state= Column(String)
    city= Column(String)
    zipcode = Column(String)
    street= Column(String)
    number= Column(String)
    complement= Column(String)
    cpf= Column(String)
    pis= Column(String)
    password = Column(String)