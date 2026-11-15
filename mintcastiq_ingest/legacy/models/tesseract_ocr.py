# models/tesseract_ocr.py

import cv2
import numpy as np
import pytesseract
from PIL import Image

TESS_CONFIG = "--psm 6 --oem 1 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.-"

def preprocess_for_ocr(img_bgr):
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    gray = cv2.fastNlMeansDenoising(gray, h=10)
    gray = cv2.equalizeHist(gray)
    gray = cv2.resize(gray, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)

    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31, 2
    )

    kernel = np.ones((2, 2), np.uint8)
    clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    return clean

def ocr_image(img_bgr) -> str:
    pre = preprocess_for_ocr(img_bgr)
    pil_img = Image.fromarray(pre)
    text = pytesseract.image_to_string(pil_img, config=TESS_CONFIG)
    return text
