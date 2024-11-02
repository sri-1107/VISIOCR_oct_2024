# OCR_APP/ocr_service.py

from PIL import Image
import os
import pytesseract
from django.core.files.storage import default_storage

def perform_ocr(image_path):
    
    image = Image.open(image_path)

    
    text = pytesseract.image_to_string(image)

    
    unwanted_phrases = ["Government of India", "Aw.", "&"]
    filtered_lines = []

   
    for line in text.splitlines():
        if not any(phrase in line for phrase in unwanted_phrases):
            filtered_lines.append(line)

    return "\n".join(filtered_lines)
