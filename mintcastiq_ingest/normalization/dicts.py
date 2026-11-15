# normalization/dicts.py

"""
Aggregates canonical vocabularies and exposes accessor functions.
This module does NOT contain the data itself — it imports from the
source-of-truth modules (teams.py, pokemon_series.py).
"""

from .teams import TEAM_CANONICAL, TEAM_MASCOT, TEAM_ABBREV
from .pokemon_series import POKEMON_SERIES

# ---------------------------------------------------------
# CLIP label lists (used by classification modules)
# ---------------------------------------------------------

TEAM_LABELS_CLIP = (
    list(TEAM_CANONICAL.keys()) +
    list(TEAM_MASCOT.keys()) +
    list(TEAM_ABBREV.keys())
)

POKEMON_SERIES_CLIP = list(POKEMON_SERIES.values())

TYPE_LABELS = [
    "sports card",
    "pokemon card",
    "trading card game card",
]

POKEMON_LABELS = [
    "Charizard", "Pikachu", "Blastoise", "Venusaur",
    "Mewtwo", "Gengar", "Bulbasaur", "Squirtle",
    "unknown pokemon",
]

# ---------------------------------------------------------
# Accessor functions (stable API for MintCastIQ)
# ---------------------------------------------------------

def get_teams():
    return TEAM_CANONICAL

def get_team_mascots():
    return TEAM_MASCOT

def get_team_abbrevs():
    return TEAM_ABBREV

def get_team_labels_clip():
    return TEAM_LABELS_CLIP

def get_pokemon_series():
    return POKEMON_SERIES

def get_pokemon_series_clip():
    return POKEMON_SERIES_CLIP

def get_type_labels():
    return TYPE_LABELS

def get_pokemon_labels():
    return POKEMON_LABELS
