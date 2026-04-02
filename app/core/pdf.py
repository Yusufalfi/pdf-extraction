from pdf2image import convert_from_path
import cv2
import numpy as np
from app.core.ocr import ocr_image
from app.config import Config

def pdf_to_text(pdf_path):
    images = convert_from_path(
        pdf_path,
        dpi=300,
        poppler_path=Config.POPPLER_PATH
    )

    full_text = ""
    for img in images:
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        full_text += "\n" + ocr_image(img_cv)

    return full_text