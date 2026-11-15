# mintcastiq_ingest/normalization/normalize.py

import re


def _clean_string(value):
    if value is None:
        return None
    if not isinstance(value, str):
        return value

    # Strip whitespace, collapse multiple spaces
    value = value.strip()
    value = re.sub(r"\s+", " ", value)

    return value


def normalize_metadata(meta: dict) -> dict:
    """
    Minimal normalization for VLM-extracted metadata.
    Only ensures:
    - all expected fields exist
    - strings are cleaned
    - booleans are safe
    - positional_hashes dict exists and is complete

    NO canonicalization.
    NO mapping.
    NO taxonomy.
    NO normalization of sets, parallels, inserts, manufacturers, or sports.
    """

    fields = {
        "player_name": None,
        "team": None,
        "position": None,

        "set_name": None,
        "set_year": None,
        "card_number": None,

        "insert_name": None,
        "print_run": None,
        "manufacturer": None,
        "sport": None,

        "rookie_card": None,
        "autograph_present": None,
        "parallel": None,

        "positional_hashes": {
            "hash_1_full": None,
            "hash_2_nw": None,
            "hash_3_n": None,
            "hash_4_ne": None,
            "hash_5_e": None,
            "hash_6_se": None,
            "hash_7_s": None,
            "hash_8_sw": None,
            "hash_9_w": None,
            "hash_10_c": None
        }
    }

    # Merge VLM output into the canonical field set
    for key in fields:
        if key == "positional_hashes":
            # ensure nested dict exists
            if "positional_hashes" in meta and isinstance(meta["positional_hashes"], dict):
                for hkey in fields["positional_hashes"]:
                    fields["positional_hashes"][hkey] = meta["positional_hashes"].get(hkey)
            continue

        if key in meta:
            fields[key] = meta[key]

    # --- Clean text fields ---
    for key in [
        "player_name", "team", "position",
        "set_name", "card_number",
        "insert_name", "print_run",
        "manufacturer", "sport",
        "parallel"
    ]:
        fields[key] = _clean_string(fields[key])

    # --- Normalize set_year to int or None ---
    if isinstance(fields["set_year"], str):
        try:
            fields["set_year"] = int(fields["set_year"])
        except ValueError:
            fields["set_year"] = None

    # --- Normalize booleans ---
    fields["rookie_card"] = bool(fields["rookie_card"]) if fields["rookie_card"] is not None else False
    fields["autograph_present"] = bool(fields["autograph_present"]) if fields["autograph_present"] is not None else False

    return fields
