import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.comments import Comment


class CommentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        track_id: uuid.UUID,
        user_id: uuid.UUID,
        timestamp_seconds: float,
        content: str,
    ) -> Comment:
        comment = Comment(
            track_id=track_id,
            user_id=user_id,
            timestamp_seconds=timestamp_seconds,
            content=content,
        )
        self.db.add(comment)
        await self.db.commit()
        await self.db.refresh(comment)
        return comment

    async def list_by_track(self, track_id: uuid.UUID, limit: int = 200) -> list[Comment]:
        stmt = (
            select(Comment)
            .where(Comment.track_id == track_id)
            .order_by(Comment.created_at.asc())
            .limit(limit)
        )
        result = await self.db.execute(stmt)
        return list(result.scalars().all())
