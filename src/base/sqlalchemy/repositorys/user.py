from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.base.sqlalchemy.models.models import User


class UserRepository():

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: schemas.User):
        db_user = User(
            name=user.name,
            email=user.email,
            country=user.country,
            state=user.state,
            city=user.city,
            zipcode=user.zipcode,
            street=user.street,
            number=user.number,
            complement=user.complement,
            cpf=user.cpf,
            pis=user.pis,
            password=user.password,
        )

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def edit(self, id: int,  user: schemas.User):
        stmt = update(User).where(User.id == id).values(
            name=user.name,
            email=user.email,
            country=user.country,
            state=user.state,
            city=user.city,
            zipcode=user.zipcode,
            street=user.street,
            number=user.number,
            complement=user.complement,
            cpf=user.cpf,
            pis=user.pis,
            password=user.password
        )
        self.session.execute(stmt)
        self.session.commit()

    def list(self):
        stmt = select(
            User.id,
            User.name,
            User.email,
            User.country,
            User.state,
            User.city,
            User.zipcode,
            User.street,
            User.number,
            User.complement,
            User.cpf,
            User.pis)
        users = self.session.execute(stmt).all()
        return users

    def getUser(self, id: str):
        stmt = select(User).where(User.id == id)
        user = self.session.execute(stmt).scalars().first()
        return user

    def searchById(self, id: int):
        query = select(
            User.id,
            User.name,
            User.email,
            User.country,
            User.state,
            User.city,
            User.zipcode,
            User.street,
            User.number,
            User.complement,
            User.cpf,
            User.pis).where(User.id == id)

        user = self.session.execute(query).first()
        return user

    def searchByCPF(self, cpf: str):
        stmt = select(
            User.id,
            User.name,
            User.email,
            User.country,
            User.state,
            User.city,
            User.zipcode,
            User.street,
            User.number,
            User.complement,
            User.cpf,
            User.pis).where(User.cpf == cpf)
        user = self.session.execute(stmt).scalars().first()
        return user

    def searchByEmail(self, email: str):
        stmt = select(
            User.id,
            User.name,
            User.email,
            User.country,
            User.state,
            User.city,
            User.zipcode,
            User.street,
            User.number,
            User.complement,
            User.cpf,
            User.pis).where(User.email == email)
        user = self.session.execute(stmt).scalars().first()
        return user

    def searchByEmailValid(self, email: str) -> User:
        stmt = select(User).where(User.email == email)
        user = self.session.execute(stmt).scalars().first()
        return user

    def delete(self, id: int):
        stmt = delete(User).where(User.id == id)

        self.session.execute(stmt)
        self.session.commit()
