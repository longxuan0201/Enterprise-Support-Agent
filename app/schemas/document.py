from typing import Any, Optional

from pydantic import BaseModel, Field


class DocumentRecord(BaseModel):
    document_id: str = Field(..., description="Unique identifier for the document")
    title: str = Field(..., description="Title of the document")
    source_type: Optional[str] = Field("manual", description="Type of the source document, e.g., 'pdf', 'webpage', etc.")
    content: str = Field(..., description="Content of the document")
    system_name: Optional[str] = Field(None, description="Name of the system that ingested the document")
    environment: Optional[str] = Field(None, description="Environment in which the document was ingested")
    tags: Optional[list[str]] = Field(default_factory=list, description="List of tags associated with the document")
    

class ChunkRecord(BaseModel):
    chunk_id: str = Field(..., description="Unique identifier for the chunk")
    document_id: str = Field(..., description="ID of the source document")
    chunk_index: int = Field(..., description="Index of the chunk within the document")
    text: str = Field(..., description="Text of the chunk")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata about the chunk")