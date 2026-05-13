
from app.llm.embedding_client import EmbeddingClient
from app.schemas.document import ChunkRecord
from app.schemas.vector import VectorDocument


def build_vector_document(chunk_record: ChunkRecord) -> VectorDocument:
    """Convert a ChunkRecord to a VectorDocument for embedding."""
    return VectorDocument(
        id=chunk_record.chunk_id,
        text=chunk_record.text,
        metadata={
            "docunment_id": chunk_record.document_id,
            **chunk_record.metadata
        }
    )
    
def build_vector_documents(chunk_records: list[ChunkRecord]) -> list[VectorDocument]:
    """Convert a list of ChunkRecords to a list of VectorDocuments."""
    return [build_vector_document(chunk) for chunk in chunk_records]

def attach_embeddings(
    documents: list[VectorDocument],
    embedding_client:EmbeddingClient
) -> list[VectorDocument]:
    """Attach embeddings to a list of VectorDocuments using the provided embedding client."""
    enriched_documents = []
    for document in documents:
        enriched_documents.append(
            VectorDocument(
                id=document.id,
                text=document.text,
                metadata=document.metadata,
                embedding=embedding_client.embed_text(document.text)  # Embed single document
            )
        )
    return enriched_documents