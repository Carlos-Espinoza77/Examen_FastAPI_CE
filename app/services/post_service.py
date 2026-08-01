from sqlalchemy.orm import Session

from app.repositories.post_repository import PostRepository
from app.schemas.post import PostCreate

class PostService:
    pass

    @staticmethod
    def get_all(db: Session):
        return PostRepository.get_all(db)

    @staticmethod
    def create(db: Session, post: PostCreate):
        return PostRepository.create(db, post)

    @staticmethod
    def update(db: Session, post_id: int, post: PostCreate):
        return PostRepository.update(db, post_id, post)

    @staticmethod
    def delete(db: Session, post_id: int):
        return PostRepository.delete(db, post_id)