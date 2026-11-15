# mintcastiq_ingest/vlm/extractor.py

from .prompts import card_meta
from .models import call_vlm


def extract_card_metadata(image_bytes: bytes) -> dict:
    """
    Given raw image bytes for a single trading card, call the vision-language
    model with the card metadata prompt and return the parsed JSON as a dict.
    """
    prompt = card_meta()
    result = call_vlm(image_bytes, prompt)

    # Expect `result` to already be a dict parsed from JSON.
    # If your model returns a JSON string, you’d do:
    #   import json
    #   result = json.loads(result)

    return result
