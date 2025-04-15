from openai import OpenAI
from config import SYSTEM_PROMPT, OPENAI_API_KEY


def call_llm(USER_PROMPT: str) -> str:
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT}
        ]
    )
    return response.choices[0].message.content