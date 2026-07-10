import qrcode
import hashlib
from datetime import datetime
from PIL import Image, ImageDraw

def generate_document(pan, org):
    data = pan + org + str(datetime.now())
    fingerprint = hashlib.sha256(data.encode()).hexdigest()

    qr = qrcode.make(fingerprint)
    qr_path = "generated/qr.png"
    qr.save(qr_path)

    img = Image.new("RGB", (600,400), "white")
    d = ImageDraw.Draw(img)

    d.text((50,50), "PAN VERIFIED DOCUMENT", fill="black")
    d.text((50,100), f"PAN: {pan}", fill="black")
    d.text((50,150), f"ORG: {org}", fill="black")
    d.text((50,200), f"Fingerprint: {fingerprint[:16]}", fill="black")

    qr_img = Image.open(qr_path)
    img.paste(qr_img, (400,100))

    path = "generated/document.png"
    img.save(path)

    return path