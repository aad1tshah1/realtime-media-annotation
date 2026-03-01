import uuid
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.track_repository import TrackRepository

class TrackService:
    def __init__(self, db: AsyncSession):
        self.repo = TrackRepository(db)

    async def create_track(self, title: str, artist: str, audio_url: str, owner_id: uuid.UUID):
        return await self.repo.create(title, artist, audio_url, owner_id)
    
    async def get_track(self, track_id: uuid.UUID):
        track = await self.repo.get_by_id(track_id)
        if not track:
            raise HTTPException(status_code=404, detail="Track not found")
        return track
    