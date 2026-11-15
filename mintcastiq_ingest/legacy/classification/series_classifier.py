# classification/series_classifier.py
from models.clip_encoder import best_label
from normalization.teams import TEAM_LABELS_CLIP, normalize_team

def predict_series(pil_img):
    label, score = best_label(pil_img, TEAM_LABELS_CLIP)
    return normalize_team(label)
