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

    @staticmethod
    def update(db: Session, comment_id: int, comment: CommentCreate):
        db_comment = db.query(Comment).filter(Comment.id == comment_id).first()

        if not db_comment:
            return None

        db_comment.content = comment.content
        db_comment.post_id = comment.post_id

        db.commit()
        db.refresh(db_comment)

        return db_comment

    @staticmethod
    def delete(db: Session, comment_id: int):
        db_comment = db.query(Comment).filter(Comment.id == comment_id).first()

        if not db_comment:
            return None

        db.delete(db_comment)
        db.commit()

        return db_comment