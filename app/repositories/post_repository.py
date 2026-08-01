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

    @staticmethod
    def update(db: Session, post_id: int, post: PostCreate):
        db_post = db.query(Post).filter(Post.id == post_id).first()

        if not db_post:
            return None

        db_post.title = post.title
        db_post.content = post.content
        db_post.user_id = post.user_id

        db.commit()
        db.refresh(db_post)

        return db_post

    @staticmethod
    def delete(db: Session, post_id: int):
        db_post = db.query(Post).filter(Post.id == post_id).first()

        if not db_post:
            return None

        db.delete(db_post)
        db.commit()

        return db_post