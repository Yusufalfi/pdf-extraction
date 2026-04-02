from app.core.pdf import pdf_to_text
from app.core.image import image_to_text
from app.service.llm_service import extract_with_llm
from app.service.validation import validate

def process_file(file_path):
    if file_path.suffix.lower() == ".pdf":
        text = pdf_to_text(file_path)
    else:
        text = image_to_text(file_path)

    if not text.strip():
        return None

    data = extract_with_llm(text)

    if not data or not validate(data):
        return None

    data["source_file"] = file_path.name
    return data