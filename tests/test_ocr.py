# test_ocr.py
import cv2
from mintcastiq_ingest.extraction.ocr_pipeline import ocr_card_regions
from mintcastiq_ingest.extraction.name_extraction import extract_player_name

img = cv2.imread("mintcastiq_ingest/tests/test_card.jpg")
text = ocr_card_regions(img)
name, cleaned, candidates = extract_player_name(img)

print("OCR:", cleaned)
print("Candidates:", candidates)
print("Player:", name)
