from sqlalchemy.orm import Session

from app.database.models import Post
from app.schemas.post import PostCreate


class PostRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(Post).all()

    @staticmethod
    def create(db: Session, post: PostCreate):
        db_post = Post(
            title=post.title,
            content=post.content,
            user_id=post.user_id,
        )

        db.add(db_post)
        db.commit()
        db.refresh(db_post)

        return db_post