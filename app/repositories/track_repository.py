import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.track import Track

class TrackRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, title: str, artist: str, audio_url: str, owner_id: uuid.UUID):
        track = Track(title=title, artist=artist, audio_url=audio_url, owner_id=owner_id)
        self.db.add(track)
        await self.db.commit()
        await self.db.refresh(track)
        return track
    
    async def get_by_id(self, track_id: uuid.UUID) -> Track | None:
        result = await self.db.execute(select(Track).where(Track.id == track_id))
        return result.scalar_one_or_none()
