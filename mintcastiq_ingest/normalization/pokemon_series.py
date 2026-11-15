# normalization/pokemon_series.py

"""
Canonical Pokémon series dictionary + normalization helpers.
This module is the single source of truth for Pokémon TCG set metadata.
"""

# ---------------------------------------------------------
# Canonical Pokémon series dictionary
# ---------------------------------------------------------

POKEMON_SERIES = {
    "par": "Paradox Rift",
    "scr": "Stellar Crown",
    "ssp": "Surging Sparks",
}

# ---------------------------------------------------------
# Normalization function
# ---------------------------------------------------------

def normalize_series(label: str) -> str | None:
    """
    Normalize CLIP/OCR Pokémon series labels into canonical names.

    Accepts:
    - set code (e.g., "par")
    - canonical name (e.g., "Paradox Rift")

    Returns:
    - canonical series name
    - None if no match
    """

    if not label:
        return None

    raw = label.strip().lower()

    # code → canonical
    if raw in POKEMON_SERIES:
        return POKEMON_SERIES[raw]

    # canonical → canonical
    for canonical in POKEMON_SERIES.values():
        if raw == canonical.lower():
            return canonical

    return None

# ---------------------------------------------------------
# Accessors
# ---------------------------------------------------------

def get_pokemon_series():
    return POKEMON_SERIES
