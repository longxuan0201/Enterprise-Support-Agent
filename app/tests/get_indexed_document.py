from app.services.vector_index_service import get_indexed_documents

docs = get_indexed_documents()
print(len(docs))
# print(docs[0].model_dump())