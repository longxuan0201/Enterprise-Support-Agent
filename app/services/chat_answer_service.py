from app.schemas.chat import ChatRequest, ChatResponse
from app.schemas.retrieval import RetrievalResponse

def generate_answer_from_retrieval(retrieval: RetrievalResponse) -> tuple[str,list[str]]:
    if not retrieval.hits:
        return (
            "I couldn't find any evidence to answer your question. Please try again with a different question.",
            [
            "Check whether the document has been ingestd",
            "Check whether the question is clear and concise"
            ]
        )
    top_hit = retrieval.hits[0]
    answer_parts = [
        f"Based on the retrieved evidence, the most relevant document is '{top_hit.metadata.get('title', 'Unknown Documnet')}'.",
        "The document describes the initial troubleshooting process for SAP interface failures in the enterprise integration environment.",
        "This answer is currently generated from the retrieved evidence rather than a llm model."
    ]
    next_steps = [
        "confirm the system name",
        "confirm the environment",
        "Check whether there was any recent change"
    ]
    return "\n".join(answer_parts), next_steps