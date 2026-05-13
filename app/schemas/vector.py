from typing import Any

from pydantic import BaseModel, Field


class VectorDocument(BaseModel):
    id: str = Field(..., description="Unique identifier for the document")
    text: str = Field(..., description="Text content of the document")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata about the document")