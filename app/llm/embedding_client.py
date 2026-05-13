from typing import Protocol

from app.schemas.vector import VectorDocument


class EmbeddingClient(Protocol):
    def embed_text(self, text:str) -> list[float]:
        """Embed a list of documents and return their vector representations."""
        ...
        
class MockEmbeddingClient:
    def embed_text(self, text: str) -> list[float]:
        """Mock embedding function that returns a fixed-size vector of zeros for each document."""
        length = float(len(text))
        line_count = float(text.count('\n') + 1)
        word_like_count = float(len(text.split()))
        return [length, line_count, word_like_count]