def get_context_from_wikipedia(query: str) -> str:
    import wikipedia
    try:
        summary = wikipedia.summary(query, sentences=5)
        return summary
    except Exception as e:
        return "No relevant context found."