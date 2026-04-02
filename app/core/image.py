import cv2
from app.core.ocr import ocr_image

def image_to_text(img_path):
    img = cv2.imread(str(img_path))
    return ocr_image(img)