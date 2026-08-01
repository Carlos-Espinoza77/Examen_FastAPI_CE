from pydantic import BaseModel

class CommentBase(BaseModel):
    content: str
    post_id: int

class CommentCreate(CommentBase):
    pass

class CommentResponse(CommentBase):
    id: int
    post_id: int

    model_config = {
        "from_attributes": True
    }

