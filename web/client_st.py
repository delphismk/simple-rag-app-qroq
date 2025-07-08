import streamlit as st
import requests

st.title("RAGドキュメントQAチャット (Groq)")

# ファイルアップロード
uploaded_file = st.file_uploader("ドキュメントをアップロード", type=["pdf", "docx", "pptx", "xlsx", "png", "jpg", "wav", "mp3"])
if uploaded_file:
    res = requests.post("http://localhost:8000/upload", files={"file": uploaded_file})
    if res.status_code == 200:
        st.success("アップロード成功")
    else:
        st.error("アップロード失敗")

# 質問送信
query = st.text_input("質問を入力してください")
if st.button("質問する") and query:
    res = requests.post("http://localhost:8000/ask", data={"query": query})
    if res.ok:
        st.write("回答:", res.json().get("answer", "[Error]"))
    else:
        st.error("回答取得に失敗しました")