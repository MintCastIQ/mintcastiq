# extraction/name_extraction.py

import re
import cv2
from PIL import Image
from mintcastiq_ingest.extraction.ocr_pipeline import ocr_card_regions
from mintcastiq_ingest.models.clip_encoder import best_label

def extract_name_candidates(text: str):
    tokens = re.findall(r"[A-Z][a-z]+", text)
    candidates = []
    for i in range(len(tokens) - 1):
        candidates.append(f"{tokens[i]} {tokens[i+1]}")
    return candidates

def pick_best_name(pil_img, candidates, min_score: float = 0.20):
    if not candidates:
        return None
    name, score = best_label(pil_img, candidates)
    return name if score >= min_score else None

def extract_player_name(crop_bgr):
    # OCR across regions
    cleaned_text = ocr_card_regions(crop_bgr)
    candidates = extract_name_candidates(cleaned_text)

    pil_img = Image.fromarray(cv2.cvtColor(crop_bgr, cv2.COLOR_BGR2RGB))
    player_name = pick_best_name(pil_img, candidates)

    return player_name, cleaned_text, candidates
