from sqlalchemy.orm import Session

from app.database.models import Comment
from app.schemas.comment import CommentCreate


class CommentRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(Comment).all()

    @staticmethod
    def create(db: Session, comment: CommentCreate):
        db_comment = Comment(
            content=comment.content,
            post_id=comment.post_id,
        )

        db.add(db_comment)
        db.commit()
        db.refresh(db_comment)

        return db_comment