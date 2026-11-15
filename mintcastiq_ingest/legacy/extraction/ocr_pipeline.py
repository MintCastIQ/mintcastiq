# extraction/ocr_pipeline.py

import re
import cv2
from mintcastiq_ingest.models.tesseract_ocr import ocr_image

NOISE_TOKENS = [
    "TOPPS", "PANINI", "DONRUSS", "CHROME", "PRIZM",
    "SELECT", "OPTIC", "STADIUM", "RC", "ROOKIE",
    "BASEBALL", "BASKETBALL", "FOOTBALL",
    "ATLANTA", "NEW YORK", "LOS ANGELES", "MIAMI",
]

def get_regions(crop_bgr):
    regions = {}

    if crop_bgr is None or crop_bgr.size == 0:
        return regions

    h, w = crop_bgr.shape[:2]

    regions["top"] = crop_bgr[0:int(0.25 * h), :]
    regions["bottom"] = crop_bgr[int(0.65 * h):h, :]
    regions["left"] = crop_bgr[:, 0:int(0.25 * w)]
    regions["right"] = crop_bgr[:, int(0.75 * w):w]

    return regions


def clean_ocr(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9 \n]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def strip_noise(text: str) -> str:
    for n in NOISE_TOKENS:
        text = text.replace(n, "")
    return text

def ocr_card_regions(crop_bgr) -> str:
    regions = get_regions(crop_bgr)
    all_text = ""

    for region in regions.values():
        if region.size == 0:
            continue
        raw = ocr_image(region)
        all_text += " " + raw

    cleaned = clean_ocr(all_text)
    cleaned = strip_noise(cleaned)
    return cleaned
                                                                                                                                                                                         
