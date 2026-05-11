from app.schemas.document import ChunkRecord
from pathlib import Path
import json

CHUNK_DIR = Path("data/chunks")
CHUNK_DIR.mkdir(parents=True, exist_ok=True)

def save_chunks(document_id: str, chunk_records: list[ChunkRecord]) -> None:
    output_path = CHUNK_DIR / f"{document_id}_chunks.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump([chunk.model_dump() for chunk in chunk_records], f, ensure_ascii=False, indent=2)