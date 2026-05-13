from typing import Protocol

from app.schemas.vector import VectorDocument


class VectorStore(Protocol):
    """Protocol for vector storage implementations."""
    
    def add_documents(self, documents: list[VectorDocument]) -> None:
        """Add a list of documents to the vector store."""
        ...
    
    def get_all_documents(self) -> list[VectorDocument]:
        """Return all documents in the vector store."""
        ...
        
class InMemoryVectorStore:
    """In-memory implementation of the VectorStore protocol for testing and development."""
    
    def __init__(self):
        self.documents: list[VectorDocument] = []
    
    def add_documents(self, documents: list[VectorDocument]) -> None:
        self.documents.extend(documents)
    
    def get_all_documents(self) -> list[VectorDocument]:
        return self.documents