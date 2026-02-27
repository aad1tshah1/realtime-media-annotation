from fastapi import FastAPI

app = FastAPI(title="Realtime Media Annotation")

@app.get("/health")
async def health():
    return {"status":"ok"}
