import uuid

from app.schemas.chat import ChatRequest, ChatResponse


async def handle_chat(request: ChatRequest) -> ChatResponse:
    session_id = str(uuid.uuid4())
    
    return ChatResponse(
        answer= f"Mock answer: I received your question -> '{request.question}'",
        session_id=session_id,
        citations=["mock://sop/sample-doc-001"],
        next_steps=[
            "confirm the system name",
            "confirm the environment",
            "Check whether there was any recent change"
        ]
    )