from fastapi import FastAPI

from app.db.session import engine
from app.models.base import Base
import app.models.track
import app.models.comments
from app.api.routes.tracks import router as track_router

app = FastAPI(title="Realtime Media Annotation")

@app.get("/health")
async def health():
    return {"status":"ok"}

@app.on_event("startup")
async def on_startup():
    # quick setup to create tables automatically
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(track_router)
