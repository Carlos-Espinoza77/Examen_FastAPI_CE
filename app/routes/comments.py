from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.comment import CommentCreate, CommentResponse
from app.services.comment_service import CommentService

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.get("/", response_model=list[CommentResponse])
def get_comments(db: Session = Depends(get_db)):
    return CommentService.get_all(db)


@router.post("/", response_model=CommentResponse)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    return CommentService.create(db, comment)

