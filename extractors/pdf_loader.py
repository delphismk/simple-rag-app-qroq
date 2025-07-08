from PyPDF2 import PdfReader
from io import BytesIO

def load_pdf_text(file_bytes: bytes) -> str:
    reader = PdfReader(BytesIO(file_bytes))
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())