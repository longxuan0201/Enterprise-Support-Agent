from typing import Optional
import uuid

from app.schemas.document import ChunkRecord, DocumentRecord


def clean_text(text: str) -> str:
    """Clean the input text by removing extra whitespace and newlines."""
    return '\n'.join(line.strip() for line in text.splitlines() if line.strip())

def chunk_text(text: str, chunk_size: int = 300, chunk_overlap: int = 50) -> list[str]:
    """Chunk the input text into smaller pieces with optional overlap."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if chunk_overlap < 0:
        raise ValueError("chunk_overlap must be non-negative")
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be less than chunk_size")
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunks.append(text[start:end])
        if end == text_length:
            break  # Reached the end of the text
        start += chunk_size - chunk_overlap  # Move start forward by chunk size minus overlap
    
    return chunks

def build_document_and_chunks(
    title: str, 
    content: str,
    source_type: str = "manual",
    system_name: Optional[str] = None,
    environment: Optional[str] = None,
    tags: Optional[list[str]] = None
    ) -> tuple[DocumentRecord, list[ChunkRecord]]:
    """Build a list of document chunks with metadata."""
    document_id = str(uuid.uuid4())
    cleaned_content = clean_text(content)
    
    document_record = DocumentRecord(
        document_id=document_id,
        title=title,
        source_type=source_type,
        content=cleaned_content,
        system_name=system_name,
        environment=environment,
        tags=tags
    )
    
    raw_chunks = chunk_text(cleaned_content)
    
    chunk_records = []
    for index, chunk in enumerate(raw_chunks):
        chunk_records.append(
            ChunkRecord(   
            chunk_id=str(uuid.uuid4()),
            document_id=document_id,
            chunk_index=index,
            text=chunk,
            metadata={
                "title": title,
                "source_type": source_type,
                "system_name": system_name,
                "environment": environment,
                "tags": tags,
                "chunk_index": index,
                "chunk_size": len(chunk)
            }
            ))
    
    return document_record, chunk_records