import uuid
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.comments_repository import CommentRepository
from app.repositories.track_repository import TrackRepository


class CommentService:
    def __init__(self, db: AsyncSession):
        self.comments = CommentRepository(db)
        self.tracks = TrackRepository(db)

    async def add_comment(
        self,
        track_id: uuid.UUID,
        user_id: uuid.UUID,
        timestamp_seconds: float,
        content: str,
    ):
        track = await self.tracks.get_by_id(track_id)
        if not track:
            raise HTTPException(status_code=404, detail="Track not found")
        return await self.comments.create(track_id, user_id, timestamp_seconds, content)

    async def list_comments(self, track_id: uuid.UUID, limit: int = 200):
        track = await self.tracks.get_by_id(track_id)
        if not track:
            raise HTTPException(status_code=404, detail="Track not found")
        return await self.comments.list_by_track(track_id, limit=limit)
