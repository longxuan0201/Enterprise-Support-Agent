import json
from pathlib import Path

from app.schemas.document import DocumentRecord

DATA_DIR = Path("data/documents")
DATA_DIR.mkdir(parents=True, exist_ok=True)

def save_document(document_record: DocumentRecord) -> None:
    
    output_path = DATA_DIR / f"{document_record.document_id}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(document_record.model_dump(), f, ensure_ascii=False, indent=2)
        