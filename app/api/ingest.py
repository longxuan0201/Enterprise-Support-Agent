from fastapi import APIRouter, Depends

from app.schemas.ingest import IngestRequest, IngestResponse
from app.services.ingest_service import handle_ingest

router = APIRouter(prefix="/ingest", tags=["ingest"])


@router.post("", response_model=IngestResponse)
async def ingest(request: IngestRequest) -> IngestResponse:
    return await handle_ingest(request)