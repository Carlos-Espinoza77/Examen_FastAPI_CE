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
