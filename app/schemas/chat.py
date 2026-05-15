from pydantic import BaseModel, Field
class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, description="User Question")

class Citation(BaseModel):
    document_id: str = Field(..., description="Document ID")
    chunk_id: str = Field(..., description="Chunk ID")
    title: str = Field(..., description="Title of the document")
    chunk_index: int = Field(..., description="Chunk index")
    score: float = Field(..., description="Score")
    source_type: str = Field(..., description="Source type of the document")
    system_name: str = Field(..., description="System name of the document")
    environment: str = Field(..., description="Environment of the document")
    tags: list[str] = Field(default_factory=list, description="Tags of the document")

class ChatResponse(BaseModel):
    answer: str = Field(..., description="Answer from the model")
    session_id:str = Field(..., description="Session ID")
    citations:list[Citation] = Field(default_factory=list, description="List of citations used to generate the answer")    
    next_steps:list[str] = Field(default_factory=list, description="List of next steps for the user to take")
    