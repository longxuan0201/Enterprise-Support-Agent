from app.llm.embedding_client import MockEmbeddingClient
from app.retrieval.vector_payload_builder import build_vector_documents, attach_embeddings
from app.schemas.retrieval import RetrievalHit, RetrievalRequest, RetrievalResponse
from app.services.vector_index_service import vector_store

embedding_client = MockEmbeddingClient()

def retrieve_evidence(request: RetrievalRequest) -> RetrievalResponse:
    query_embedding = embedding_client.embed_text(request.query)
    results = vector_store.search(query_embedding, request.top_k)

    hits = [
        RetrievalHit(
            id=document.id,
            text=document.text,
            metadata=document.metadata,
            score=score
        )
        for document, score in results
    ]

    return RetrievalResponse(
        query=request.query,
        top_k=request.top_k,
        hits=hits
    )