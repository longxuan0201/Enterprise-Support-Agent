from fastapi import FastAPI
from app.api.ingest import router as ingest_router
from app.api.chat import router as chat_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

# Health check endpoint
@app.get("/health", tags=["system"])
async def health_check() -> dict:
    return {
        "status": "ok", 
        "app_name": settings.app_name, 
        "version": settings.app_version
        }

app.include_router(ingest_router)
app.include_router(chat_router)