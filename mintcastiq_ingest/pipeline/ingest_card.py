# mintcastiq_ingest/pipeline/ingest_card.py

import os

from mintcastiq_ingest.vlm.extractor import extract_card_metadata
from mintcastiq_ingest.normalization.filename_builder import build_filename
from mintcastiq_ingest.normalization.dicts import normalize_metadata


def ingest_card(image_path: str) -> str:
    """
    Process a single trading card image:
    - load image bytes
    - extract metadata using the VLM
    - normalize metadata fields
    - build a deterministic filename
    - rename the file on disk
    - return the new filename
    """

    # 1. Load image bytes
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    # 2. Extract metadata via VLM
    raw_meta = extract_card_metadata(image_bytes)

    # 3. Normalize metadata (names, sets, teams, card numbers)
    meta = normalize_metadata(raw_meta)

    # 4. Build filename from normalized metadata
    new_filename = build_filename(meta)

    # 5. Compute new path
    dirpath = os.path.dirname(image_path)
    new_path = os.path.join(dirpath, new_filename)

    # 6. Rename file
    os.rename(image_path, new_path)

    return new_path
