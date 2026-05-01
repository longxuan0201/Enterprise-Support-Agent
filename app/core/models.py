from pydantic import BaseModel, Field
from typing import Optional

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, description="User Question")
    
class ChatResponse(BaseModel):
    answer: str = Field(..., description="Answer from the model")
    source: Optional[str] = Field(None, description="Source of the answer, if available")
    session_id:str
    citations:list[str] = Field([], description="List of citations used to generate the answer")    
    next_steps:list[str] = Field([], description="List of next steps for the user to take")
    
class IngestRequest(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the document")
    content: str = Field(..., min_length=1, description="Content of the document")
    source_type: Optional[str] = Field("manual", description="Type of the source document, e.g., 'pdf', 'webpage', etc.")
    
class IngestResponse(BaseModel):
    message: str = Field(..., description="Result of the ingestion process")
    document_id: str = Field(..., description="ID of the ingested document, if successful")
    title: str = Field(..., description="Title of the ingested document")