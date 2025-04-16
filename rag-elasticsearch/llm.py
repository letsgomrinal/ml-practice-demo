import openai
openai.api_key = "your-openai-key"

def ask_llm(query, retrieved_chunks):
    context = "\n\n".join(retrieved_chunks)
    prompt = f"Context:\n{context}\n\nQuestion: {query}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
