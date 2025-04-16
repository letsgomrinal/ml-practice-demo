from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch

model = SentenceTransformer("all-MiniLM-L6-v2")

#print(SentenceTransformer("all-MiniLM-L6-v2")._target_device)
es = Elasticsearch("http://localhost:9200",headers={"Content-Type": "application/json"})

def index_chunks(index_name, chunks):
    embeddings = model.encode(chunks)
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        doc = {
            "text": chunk,
            "embedding": emb.tolist()
        }
        es.index(index=index_name, id=f"chunk_{i}", document=doc)

if __name__ == "__main__":
    index_name = "pdf_rag_chunks"
    chunks = [
        "This is the first chunk.",
        "This is the second chunk.",
        "This is the third chunk.",
    ]
    index_chunks(index_name, chunks)
