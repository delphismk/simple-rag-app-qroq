from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from core.embedder import embedding_model

persist_dir = "chroma_db"

vectorstore = Chroma(
    persist_directory=persist_dir,
    embedding_function=embedding_model
)

def store_document(filename: str, content: str):
    doc = Document(
        page_content=content,
        metadata={"source": filename}
    )
    vectorstore.add_documents([doc])

def get_retriever():
    return vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

def retrieve_context(query: str) -> str:
    docs = vectorstore.similarity_search(query, k=3)
    return "\n\n".join([doc.page_content for doc in docs])