from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.post import PostCreate, PostResponse
from app.services.post_service import PostService

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)

@router.get("/", response_model=list[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    return PostService.get_all(db)

@router.post("/", response_model=PostResponse)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
):
    return PostService.create(db, post)

@router.put("/{post_id}", response_model=PostResponse)
def update_post(
    post_id: int,
    post: PostCreate,
    db: Session = Depends(get_db),
):
    return PostService.update(db, post_id, post)


@router.delete("/{post_id}")
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
):
    PostService.delete(db, post_id)
    return {"message": "Post eliminado"}