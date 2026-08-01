from sqlalchemy.orm import Session

from app.database.models import User
from app.schemas.user import UserCreate

class UserRepository:
    pass

    @staticmethod
    def get_all(db: Session):
        return db.query(User).all()

    @staticmethod
    def get_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def create(db: Session, user: UserCreate):
        db_user = User(
            name=user.name,
            email=user.email,
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def update(db: Session, user_id: int, user: UserCreate):
        db_user = db.query(User).filter(User.id == user_id).first()

        if not db_user:
            return None

        db_user.name = user.name
        db_user.email = user.email

        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def delete(db: Session, user_id: int):
        db_user = db.query(User).filter(User.id == user_id).first()

        if not db_user:
            return None

        db.delete(db_user)
        db.commit()

        return db_user