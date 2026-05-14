from typing import Any

from pydantic import BaseModel, Field


class RetrievalRequest(BaseModel):
    query: str = Field(..., min_length=1, description="The user's query for document retrieval")
    top_k: int = Field(5, ge=1, le=10, description="The number of top documents to retrieve")
    
class RetrievalHit(BaseModel):
    id: str = Field(..., description="Unique identifier of the retrieved document")
    text: str = Field(..., description="The text content of the retrieved document")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata about the retrieved document")
    score: float = Field(..., description="The relevance score of the retrieved document")
    
class RetrievalResponse(BaseModel):
    query: str = Field(..., description="The original query that was processed")
    top_k: int = Field(..., description="The number of top documents that were requested for retrieval")
    hits: list[RetrievalHit] = Field(..., description="List of retrieved documents matching the query")