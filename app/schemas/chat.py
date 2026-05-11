from pydantic import BaseModel, Field
class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, description="User Question")
    
class ChatResponse(BaseModel):
    answer: str = Field(..., description="Answer from the model")
    session_id:str = Field(..., description="Session ID")
    citations:list[str] = Field(default_factory=list, description="List of citations used to generate the answer")    
    next_steps:list[str] = Field(default_factory=list, description="List of next steps for the user to take")
    