from fastapi import APIRouter

from app.schemas.retrieval import RetrievalRequest, RetrievalResponse
from app.services.retrieval_service import retrieve_evidence

router = APIRouter(prefix="/retrieve", tags=["retrieve"])

@router.post("", response_model=RetrievalResponse)
async def retrieve(request: RetrievalRequest) -> RetrievalResponse:
    return retrieve_evidence(request)