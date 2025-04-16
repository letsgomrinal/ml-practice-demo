# Start ElasticSearch with Kibana:

```bash
docker run -d --name kibana-rag \
  --link elastic-rag:elasticsearch \
  -p 5601:5601 \
  -e "ELASTICSEARCH_HOSTS=http://elasticsearch:9200" \
  docker.elastic.co/kibana/kibana:8.12.2
```

# Step-1 : Create an index

- Go to `kibana` console:
http://localhost:5601/app/dev_tools#/console

- create an index:

```bash
PUT pdf_rag_chunks
{
  "mappings": {
    "properties": {
      "text": { "type": "text" },
      "embedding": {
        "type": "dense_vector",
        "dims": 384,
        "index": true,
        "similarity": "cosine"
      }
    }
  }
}
```

Sample response:

```bash
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "pdf_rag_chunks"
}
```



# Note:

- Ran into some hiccups because TF library:

```
pip uninstall tensorflow tensorflow-cpu tensorflow-gpu keras
```

- (2) Install pytorch:
```
pip install torch torchvision
pip install sentence-transformers --no-deps
```
