from PIL import Image
import pytesseract
from io import BytesIO

def extract_text_from_image(file_bytes: bytes) -> str:
    image = Image.open(BytesIO(file_bytes))
    return pytesseract.image_to_string(image, lang="jpn+eng")