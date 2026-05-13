from app.retrieval.ingest_pipeline import build_document_and_chunks
from app.schemas.ingest import IngestRequest, IngestResponse
from app.storage.chunk_store import save_chunks
from app.storage.document_store import save_document


async def handle_ingest(request: IngestRequest) -> IngestResponse:
    document, chunk = build_document_and_chunks(
        title=request.title,
        content=request.content,
        source_type=request.source_type or "manual",
        system_name=request.system_name,
        environment=request.environment,
        tags=request.tags
    )
    save_document(document)
    save_chunks(document.document_id, chunk)
    
    
    return IngestResponse(
        message="Document ingested successfully with {} chunks".format(len(chunk)),
        document_id=document.document_id,
        title=request.title
        )