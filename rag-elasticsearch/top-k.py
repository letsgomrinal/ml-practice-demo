def search_similar_chunks(query, index_name="pdf_rag_chunks", top_k=5):
    query_vec = model.encode([query])[0].tolist()

    script_query = {
        "size": top_k,
        "query": {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                    "params": {"query_vector": query_vec}
                }
            }
        }
    }

    response = es.search(index=index_name, body=script_query)
    return [hit["_source"]["text"] for hit in response["hits"]["hits"]]
