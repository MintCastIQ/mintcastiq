# classification/team_classifier.py

"""
Team classifier module.
Current implementation uses CLIP similarity scoring against TEAM_LABELS_CLIP.
Later, this module will load a trained classifier (logistic regression or MLP)
and fall back to CLIP when confidence is low.
"""

from models.clip_encoder import best_label
from normalization.dicts import get_team_labels_clip
from normalization.teams import normalize_team


def predict_team(pil_img):
    """
    Predict the canonical team name for a sports card.

    Steps:
    1. Get CLIP label list (canonical + mascots + abbrevs).
    2. Use CLIP to pick the best label.
    3. Normalize the label to a canonical team name.
    4. Return None if normalization fails.
    """

    labels = get_team_labels_clip()
    raw_label, score = best_label(pil_img, labels)

    # Normalize to canonical team name
    team = normalize_team(raw_label)

    return team
