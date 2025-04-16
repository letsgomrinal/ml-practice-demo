from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
index_name = "pdf_rag_chunks"

def create_index_if_not_exists():
    if not es.indices.exists(index=index_name):
        mapping = {
            "mappings": {
                "properties": {
                    "text": {"type": "text"},
                    "embedding": {
                        "type": "dense_vector",
                        "dims": 384,
                        "index": True,
                        "similarity": "cosine"
                    }
                }
            }
        }
        es.indices.create(index=index_name, body=mapping)
        print(f"✅ Index '{index_name}' created.")
    else:
        print(f"⚠️ Index '{index_name}' already exists.")
