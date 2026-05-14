from app.retrieval.ingest_pipeline import build_document_and_chunks
from app.schemas.ingest import IngestRequest, IngestResponse
from app.services.vector_index_service import index_chunks
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
    
    indexed_count = index_chunks(chunk)
    
    return IngestResponse(
        message=f"Document ingested successfully with {len(chunk)} chunks and {indexed_count} indexed vectors.",
        document_id=document.document_id,
        title=request.title
        )