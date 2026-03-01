import uuid
from pydantic import BaseModel, HttpUrl

class TrackCreate(BaseModel):
    title: str
    artist: str
    audio_url: HttpUrl    

class TrackOut(BaseModel):
    id: uuid.UUID
    title: str
    artist: str
    audio_url: str
    owner_id: uuid.UUID

