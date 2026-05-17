from typing import Optional
import uuid

from app.schemas.document import ChunkRecord, DocumentRecord

## v1 清洗策略
def clean_text(text: str) -> str:
    """Clean the input text by removing extra whitespace and newlines."""
    return '\n'.join(line.strip() for line in text.splitlines() if line.strip())

def find_chunk_end_boundary(text: str, start:int, end:int) -> int:
    """Find the boundaries of the chunks in the text."""
    boundaries_candidates = ["\n",".",",","!", "?", ";", ":", " "]
    search_window=text[start:end]
    best_boundary = -1
    for marker in boundaries_candidates:
        pos = search_window.rfind(marker)
        if pos > best_boundary:
            best_boundary = pos
    if best_boundary == -1:
        return end
    adjusted_end=start + best_boundary + 1

    if adjusted_end - start < 100:
            return end
    return adjusted_end

def find_chunk_start_boundary(text: str, start: int, end: int) -> int:
    """
    Adjust the chunk start position forward to the nearest natural boundary
    within a small window, to avoid starting in the middle of a word.
    """
    boundary_candidates = ["\n", " "]
    search_window = text[start:end]

    best_boundary = -1
    for marker in boundary_candidates:
        pos = search_window.find(marker)
        if pos != -1 and (best_boundary == -1 or pos < best_boundary):
            best_boundary = pos

    if best_boundary == -1:
        return start

    adjusted_start = start + best_boundary + 1

    # 防止移动太多导致 overlap 基本失效
    if adjusted_start - start > 30:
        return start

    return adjusted_start

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
        optimal_end = find_chunk_end_boundary(text, start, end)
         # 防止边界优化失败时出现死循环
        if optimal_end <= start:
            optimal_end = end

        chunk = text[start:optimal_end]
        chunks.append(chunk)
        if optimal_end >= text_length:
            break  # Reached the end of the text
        next_start = max(optimal_end - chunk_overlap, 0)
        next_start = find_chunk_start_boundary(text, next_start, min(next_start + 50, text_length))

        if next_start <= start:
            next_start = max(optimal_end - chunk_overlap, 0) # Move start forward by chunk size minus overlap
        start = next_start # Move start forward by chunk size minus overlap
    
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