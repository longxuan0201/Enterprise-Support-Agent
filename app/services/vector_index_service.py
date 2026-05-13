from app.llm.embedding_client import MockEmbeddingClient
from app.retrieval.vector_payload_builder import attach_embeddings, build_vector_documents
from app.retrieval.vector_payload_builder import build_vector_documents
from app.schemas.document import ChunkRecord
from app.storage.vector_storage import InMemoryVectorStore


embedding_client = MockEmbeddingClient()
vector_store = InMemoryVectorStore()

def index_chunks(chunks: list[ChunkRecord]) -> int:
    """Convert chunks to vector documents, attach embeddings, and store them."""
    vector_documents = build_vector_documents(chunks)
    enriched_documents = attach_embeddings(vector_documents, embedding_client)
    vector_store.add_documents(enriched_documents)
    return len(enriched_documents)

def get_indexed_documents():
    """Retrieve all indexed documents from the vector store."""
    return vector_store.get_all_documents()