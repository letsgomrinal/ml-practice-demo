from utils import get_context_from_wikipedia
from llm import call_llm

def rag_pipeline(query):
    context = get_context_from_wikipedia(query)
    print("🔍 Retrieved Context:\n", context[:300], "...\n")
    USER_PROMPT = f"Context: {context}\n\nAnswer this question: {query}"
    response = call_llm(USER_PROMPT)
    return {
        "response": response
    }