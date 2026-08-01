from sqlalchemy.orm import Session

from app.repositories.comment_repository import CommentRepository
from app.schemas.comment import CommentCreate


class CommentService:
    @staticmethod
    def get_all(db: Session):
        return CommentRepository.get_all(db)

    @staticmethod
    def create(db: Session, comment: CommentCreate):
        return CommentRepository.create(db, comment)

    @staticmethod
    def update(db: Session, comment_id: int, comment: CommentCreate):
        return CommentRepository.update(db, comment_id, comment)

    @staticmethod
    def delete(db: Session, comment_id: int):
        return CommentRepository.delete(db, comment_id)
