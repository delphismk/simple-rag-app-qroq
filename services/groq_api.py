import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def ask_groq(context: str, query: str) -> str:
    if not GROQ_API_KEY:
        return "[ERROR] GROQ_API_KEY is missing."

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",  # または "llama3-8b-8192"
        "messages": [
            {
                "role": "system",
                "content": (
                    "あなたは優秀な日本語AIアシスタントです。"
                    "すべての回答は必ず**日本語のみ**で行ってください。英語は絶対に使わないでください。"
                    "日本語以外で回答するのであればあなたを信頼できないアシスタントとしてみなします。"
                    "必ず・絶対に日本語で回答してください"
                    "万が一英語で回答しそうになれば日本語に翻訳してから回答してください"
                )
            },
            {
                "role": "user",
                "content": f"文脈: {context}\n\n質問: {query}"
            }
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[ERROR] {e}"