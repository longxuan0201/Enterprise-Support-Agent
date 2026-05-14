import math
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

def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be of the same length")
    
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in vec1))
    magnitude2 = math.sqrt(sum(b ** 2 for b in vec2))
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    return dot_product / (magnitude1 * magnitude2)

class InMemoryVectorStore:
    """In-memory implementation of the VectorStore protocol for testing and development."""
    
    def __init__(self):
        self.documents: list[VectorDocument] = []
    
    def add_documents(self, documents: list[VectorDocument]) -> None:
        self.documents.extend(documents)
    
    def get_all_documents(self) -> list[VectorDocument]:
        return self.documents
    
    def search(self, query_embedding: list[float], top_k: int = 3) -> list[tuple[VectorDocument, float]]:
        """Search for the most similar documents to the query embedding."""
        scored_documents = []
        for doc in self.documents:
            if doc.embedding is not None:
                score = cosine_similarity(query_embedding, doc.embedding)
                scored_documents.append((doc, score))
        
        scored_documents.sort(key=lambda x: x[1], reverse=True)
        return  scored_documents[:top_k]