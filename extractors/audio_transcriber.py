import whisper
from tempfile import NamedTemporaryFile

model = whisper.load_model("base")

def transcribe_audio(file_bytes: bytes) -> str:
    with NamedTemporaryFile(delete=True, suffix=".mp3") as tmp:
        tmp.write(file_bytes)
        tmp.flush()
        result = model.transcribe(tmp.name, language="ja")
    return result["text"]