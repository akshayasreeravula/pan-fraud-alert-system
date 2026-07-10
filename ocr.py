import pytesseract
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\mohan\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def extract_pan(path):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    match = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]{1}", text)
    if match:
        return match.group(0)
    return "NOT_FOUND"