from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    user_id: int

    model_config = {
        "from_attributes": True
    }

