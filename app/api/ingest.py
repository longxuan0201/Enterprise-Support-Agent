from fastapi import APIRouter, Depends
from app.core.models import IngestRequest, IngestResponse
import uuid
from pathlib import Path
import json

router = APIRouter(prefix="/ingest", tags=["ingest"])

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

@router.post("", response_model=IngestResponse)
async def ingest(request: IngestRequest) -> IngestResponse:
    document_id = str(uuid.uuid4())
    
    payload = {
        "document_id": document_id,
        "title": request.title,
        "content": request.content,
        "source_type": request.source_type
    }
    
    output_path = DATA_DIR / f"{document_id}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        
        return IngestResponse(
            message="Document ingested successfully",
            document_id=document_id,
            title=request.title
        )