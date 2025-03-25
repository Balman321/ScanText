from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
import pytesseract
from PIL import Image

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены, для продакшн укажите конкретный домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    return {"text": text}