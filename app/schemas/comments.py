import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class CommentCreate(BaseModel):
    timestamp_seconds: float = Field(ge=0)
    content: str = Field(min_length=1, max_length=2000)


class CommentOut(BaseModel):
    id: uuid.UUID
    track_id: uuid.UUID
    user_id: uuid.UUID
    timestamp_seconds: float
    content: str
    created_at: datetime
