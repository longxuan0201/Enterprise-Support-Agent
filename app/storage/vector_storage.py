from typing import Protocol

from app.schemas.vector import VectorDocument


class VectorStore(Protocol):
    """Protocol for vector storage implementations."""
    
    def add_documents(self, documents: list[VectorDocument]) -> None:
        """Add a list of documents to the vector store."""
        ...
    
    def query(self, query_vector: list[float], top_k: int = 5) -> list[VectorDocument]:
        """Query the vector store with a vector and return the top K most similar documents."""
        ...
        
class InMemoryVectorStore:
    """In-memory implementation of the VectorStore protocol for testing and development."""
    
    def __init__(self):
        self.documents: list[VectorDocument] = []
    
    def add_documents(self, documents: list[VectorDocument]) -> None:
        self.documents.extend(documents)
    
    def query(self, query_vector: list[float], top_k: int = 5) -> list[VectorDocument]:
        # This is a mock implementation that returns the first K documents regardless of the query vector
        return self.documents[:top_k]