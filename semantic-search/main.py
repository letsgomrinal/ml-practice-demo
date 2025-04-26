from config import EMBEDDING_MODEL
from typing import List

def get_embeddings(data:List):

    from sentence_transformers import SentenceTransformer 
    model = SentenceTransformer(EMBEDDING_MODEL)
    e = model.encode(data)
    return e

def get_similarity(query_embedding,corpus_embeddings):
    from sklearn.metrics.pairwise import cosine_similarity
    sim_score = cosine_similarity(query_embedding,corpus_embeddings).flatten()
    return sim_score
    
def get_topk_indices(similarity_scores,top_k):
    top_k_indices = similarity_scores.argsort()[::-1][:top_k].tolist()
    return top_k_indices 

def get_topk_docs(corpus,query,top_k):
    corpus_emb = get_embeddings(corpus)
    query_emb = get_embeddings([query])
    sim_scores = get_similarity(query_emb,corpus_emb)
    indices = get_topk_indices(sim_scores,top_k)

    response = []
    for i in indices:
        response.append(corpus[i])
    return response 

if __name__=='__main__':
    corpus = [
        'the cat sits outside', 
        'the new moview is awesome', 
        'the new movie is really great', 
        'the dog bark on stangers'
        ]
    query = "how was the movie?"
    top_k = 2
    get_topk_docs(corpus,query,top_k)




