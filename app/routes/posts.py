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