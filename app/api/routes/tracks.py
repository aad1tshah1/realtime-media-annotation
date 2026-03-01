import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_current_user_id
from app.db.session import get_db
from app.schemas.track import TrackCreate, TrackOut
from app.services.track_service import TrackService

router = APIRouter(prefix="/tracks", tags=["tracks"])


@router.post("", response_model=TrackOut)
async def create_track(
    payload: TrackCreate,
    db: AsyncSession = Depends(get_db),
    user_id: uuid.UUID = Depends(get_current_user_id),
):
    service = TrackService(db)
    return await service.create_track(
        title=payload.title,
        artist=payload.artist,
        audio_url=str(payload.audio_url),
        owner_id=user_id,
    )


@router.get("/{track_id}", response_model=TrackOut)
async def get_track(track_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    service = TrackService(db)
    return await service.get_track(track_id)
