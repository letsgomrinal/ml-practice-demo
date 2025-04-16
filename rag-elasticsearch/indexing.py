from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch

model = SentenceTransformer("all-MiniLM-L6-v2")

# Correct ES connection (no headers, request_timeout used)
es = Elasticsearch(
    hosts=["http://localhost:9200"],
    request_timeout=60
)

def index_chunks(index_name, chunks):
    embeddings = model.encode(chunks)
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        doc = {
            "text": chunk,
            "embedding": emb.tolist()
        }
        es.index(index=index_name, id=f"chunk_{i}", document=doc)  # ES v8+

if __name__ == "__main__":
    index_name = "pdf_rag_chunks"
    chunks = [
        "This is the first chunk.",
        "This is the second chunk.",
        "This is the third chunk.",
    ]
    index_chunks(index_name, chunks)
