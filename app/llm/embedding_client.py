from typing import Protocol

from app.schemas.vector import VectorDocument


class EmbeddingClient(Protocol):
    def embed_documents(self, documents: list[VectorDocument]) -> list[list[float]]:
        """Embed a list of documents and return their vector representations."""
        ...
        
class MockEmbeddingClient:
    def embed_documents(self, documents: list[VectorDocument]) -> list[list[float]]:
        """Mock embedding function that returns a fixed-size vector of zeros for each document."""
        return [[0.0] * 768 for _ in documents]