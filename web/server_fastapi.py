from fastapi import FastAPI, UploadFile, File, Form
from extractors.router import extract_text
from core.qa_chain import get_answer
from core.vectorstore import store_document

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    filename = file.filename
    content = await file.read()
    extracted = extract_text(content, filename)
    # 🔻 extracted をすぐに vectorstore に格納
    store_document(filename, extracted)
    return {"message": "Uploaded."}

@app.post("/ask")
async def ask(query: str = Form(...)):
    return {"answer": get_answer(query)}  # ← 余計なチェック削除