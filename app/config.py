import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv("GEMINI_API_KEY")

    INPUT_FOLDER = "data/input/File_PDF_FAKE"
    OUTPUT_FILE = "data/output/result.xlsx"

    POPPLER_PATH = r"D:\yusuf-python\poppler-25.12.0\Library\bin"
    TESSERACT_PATH = r"C:\Users\yalfi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

    MAX_RETRY = 3