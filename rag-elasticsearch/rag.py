from indexing import index_chunks
from top_k import search_similar_chunks
from llm import ask_llm
from preprocess import load_pdf_text, chunk_text

def rag_pipeline_with_elastic(pdf_path, query):
    text = load_pdf_text(pdf_path)
    chunks = chunk_text(text)
    index_chunks("pdf_rag_chunks", chunks)
    retrieved = search_similar_chunks(query)
    answer = ask_llm(query, retrieved)

    print("🔍 Top-K Context:\n", "\n---\n".join(retrieved))
    print("\n🧠 Answer:\n", answer)
