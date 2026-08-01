from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate

class UserService:
    pass

    @staticmethod
    def get_all(db: Session):
        return UserRepository.get_all(db)
    
    @staticmethod
    def get_by_id(db: Session, user_id: int):
        return UserRepository.get_by_id(db, user_id)

    @staticmethod
    def create(db: Session, user: UserCreate):
        return UserRepository.create(db, user)

    @staticmethod
    def update(db: Session, user_id: int, user: UserCreate):
        return UserRepository.update(db, user_id, user)

    @staticmethod
    def delete(db: Session, user_id: int):
        return UserRepository.delete(db, user_id)
