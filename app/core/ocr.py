import pytesseract
from app.config import Config
from app.core.preprocess import preprocess_image
pytesseract.pytesseract.tesseract_cmd = Config.TESSERACT_PATH

print("TESSERACT PATH:", pytesseract.pytesseract.tesseract_cmd)

def ocr_image(img):
    processed = preprocess_image(img)
    return pytesseract.image_to_string(processed, lang="eng+deu")