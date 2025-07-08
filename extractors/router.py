from .pdf_loader import load_pdf_text
from .docx_loader import load_docx_text
from .pptx_loader import load_pptx_text
from .xlsx_loader import load_xlsx_text
from .image_ocr import extract_text_from_image
from .audio_transcriber import transcribe_audio

def extract_text(file_bytes: bytes, filename: str) -> str:
    filename = filename.lower()

    if filename.endswith(".pdf"):
        return load_pdf_text(file_bytes)
    elif filename.endswith(".docx"):
        return load_docx_text(file_bytes)
    elif filename.endswith(".pptx"):
        return load_pptx_text(file_bytes)
    elif filename.endswith(".xlsx"):
        return load_xlsx_text(file_bytes)
    elif filename.endswith((".png", ".jpg", ".jpeg")):
        return extract_text_from_image(file_bytes)
    elif filename.endswith((".wav", ".mp3")):
        return transcribe_audio(file_bytes)
    else:
        return "対応していないファイル形式です"