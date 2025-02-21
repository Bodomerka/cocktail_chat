import faiss
import numpy as np
from langchain_openai import OpenAIEmbeddings
import os

class VectorStore:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
        self.index = faiss.IndexFlatL2(1536)  # OpenAI embeddings are 1536-dimensional
        self.metadata = []  # Store metadata alongside vectors

    def add_cocktails(self, cocktails):
        texts = [f"{c['name']}: {', '.join(c['ingredients'])}" for c in cocktails]
        vectors = self.embeddings.embed_documents(texts)
        self.index.add(np.array(vectors, dtype="float32"))
        self.metadata.extend([{"name": c["name"], "ingredients": c["ingredients"]} for c in cocktails])

    def add_user_preference(self, text):
        vector = self.embeddings.embed_query(text)
        self.index.add(np.array([vector], dtype="float32"))
        self.metadata.append({"type": "preference", "text": text})

    def search(self, query, k=5):
        query_vector = self.embeddings.embed_query(query)
        distances, indices = self.index.search(np.array([query_vector], dtype="float32"), k)
        return [self.metadata[i] for i in indices[0]]

vector_store = VectorStore()