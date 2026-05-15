import uuid

from app.schemas.chat import ChatRequest, ChatResponse, Citation
from app.schemas.retrieval import RetrievalRequest
from app.services.chat_answer_service import generate_answer_from_retrieval
from app.services.retrieval_service import retrieve_evidence


async def handle_chat(request: ChatRequest) -> ChatResponse:
    session_id = str(uuid.uuid4())

    retrieval_request = RetrievalRequest(
        query=request.question,
        top_k=3
    )
    retrieval_result = retrieve_evidence(retrieval_request)
    answer, next_steps = generate_answer_from_retrieval(retrieval_result)
    citations = []
    for hit in retrieval_result.hits:
        metadata = hit.metadata
        citations.append(
            Citation(
                chunk_id=hit.id,
                document_id=metadata.get('document_id', ''),
                title=metadata.get('title', 'Unknown Document'),
                chunk_index=metadata.get('chunk_index', -1),
                score=hit.score,
                source_type=metadata.get("source_type"),
                system_name=metadata.get("system_name"),
                environment=metadata.get("environment"),
                tags=metadata.get("tags", [])
        ))
    return ChatResponse(
        answer= answer,
        session_id=session_id,
        citations=citations,
        next_steps=next_steps
    )