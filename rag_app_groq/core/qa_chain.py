from core.vectorstore import retrieve_context
from services.groq_api import ask_groq

def get_answer(query: str) -> str:
    context = retrieve_context(query)
    return ask_groq(context, query)