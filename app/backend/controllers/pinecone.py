from src.pinecone_helpers import query, upload

class PineconeController:
    def query(text, filter, namespace, top_k=10):
        return query(text, filter, namespace, top_k)

    def upload(text, metadata, namespace):
        return upload(text, metadata, namespace)