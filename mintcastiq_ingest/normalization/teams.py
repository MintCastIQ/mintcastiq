# normalization/teams.py

"""
Canonical team dictionaries + normalization helpers.
This module is the single source of truth for all sports team metadata.
"""

# -----------------------------
# Canonical team dictionary
# -----------------------------

TEAM_CANONICAL = {
    # MLB
    "Arizona Diamondbacks": {"city": "Arizona", "mascot": "Diamondbacks", "league": "MLB"},
    "Atlanta Braves": {"city": "Atlanta", "mascot": "Braves", "league": "MLB"},
    "Baltimore Orioles": {"city": "Baltimore", "mascot": "Orioles", "league": "MLB"},
    "Boston Red Sox": {"city": "Boston", "mascot": "Red Sox", "league": "MLB"},
    "Chicago Cubs": {"city": "Chicago", "mascot": "Cubs", "league": "MLB"},
    "Chicago White Sox": {"city": "Chicago", "mascot": "White Sox", "league": "MLB"},
    "Cincinnati Reds": {"city": "Cincinnati", "mascot": "Reds", "league": "MLB"},
    "Cleveland Guardians": {"city": "Cleveland", "mascot": "Guardians", "league": "MLB"},
    "Colorado Rockies": {"city": "Colorado", "mascot": "Rockies", "league": "MLB"},
    "Detroit Tigers": {"city": "Detroit", "mascot": "Tigers", "league": "MLB"},
    "Houston Astros": {"city": "Houston", "mascot": "Astros", "league": "MLB"},
    "Kansas City Royals": {"city": "Kansas City", "mascot": "Royals", "league": "MLB"},
    "Los Angeles Angels": {"city": "Los Angeles", "mascot": "Angels", "league": "MLB"},
    "Los Angeles Dodgers": {"city": "Los Angeles", "mascot": "Dodgers", "league": "MLB"},
    "Miami Marlins": {"city": "Miami", "mascot": "Marlins", "league": "MLB"},
    "Milwaukee Brewers": {"city": "Milwaukee", "mascot": "Brewers", "league": "MLB"},
    "Minnesota Twins": {"city": "Minnesota", "mascot": "Twins", "league": "MLB"},
    "New York Mets": {"city": "New York", "mascot": "Mets", "league": "MLB"},
    "New York Yankees": {"city": "New York", "mascot": "Yankees", "league": "MLB"},
    "Oakland Athletics": {"city": "Oakland", "mascot": "Athletics", "league": "MLB"},
    "Philadelphia Phillies": {"city": "Philadelphia", "mascot": "Phillies", "league": "MLB"},
    "Pittsburgh Pirates": {"city": "Pittsburgh", "mascot": "Pirates", "league": "MLB"},
    "San Diego Padres": {"city": "San Diego", "mascot": "Padres", "league": "MLB"},
    "San Francisco Giants": {"city": "San Francisco", "mascot": "Giants", "league": "MLB"},
    "Seattle Mariners": {"city": "Seattle", "mascot": "Mariners", "league": "MLB"},
    "St. Louis Cardinals": {"city": "St. Louis", "mascot": "Cardinals", "league": "MLB"},
    "Tampa Bay Rays": {"city": "Tampa Bay", "mascot": "Rays", "league": "MLB"},
    "Texas Rangers": {"city": "Texas", "mascot": "Rangers", "league": "MLB"},
    "Toronto Blue Jays": {"city": "Toronto", "mascot": "Blue Jays", "league": "MLB"},
    "Washington Nationals": {"city": "Washington", "mascot": "Nationals", "league": "MLB"},

    # NBA
    "Atlanta Hawks": {"city": "Atlanta", "mascot": "Hawks", "league": "NBA"},
    "Boston Celtics": {"city": "Boston", "mascot": "Celtics", "league": "NBA"},
    "Brooklyn Nets": {"city": "Brooklyn", "mascot": "Nets", "league": "NBA"},
    "Charlotte Hornets": {"city": "Charlotte", "mascot": "Hornets", "league": "NBA"},
    "Chicago Bulls": {"city": "Chicago", "mascot": "Bulls", "league": "NBA"},
    "Cleveland Cavaliers": {"city": "Cleveland", "mascot": "Cavaliers", "league": "NBA"},
    "Dallas Mavericks": {"city": "Dallas", "mascot": "Mavericks", "league": "NBA"},
    "Denver Nuggets": {"city": "Denver", "mascot": "Nuggets", "league": "NBA"},
    "Detroit Pistons": {"city": "Detroit", "mascot": "Pistons", "league": "NBA"},
    "Golden State Warriors": {"city": "Golden State", "mascot": "Warriors", "league": "NBA"},
    "Houston Rockets": {"city": "Houston", "mascot": "Rockets", "league": "NBA"},
    "Indiana Pacers": {"city": "Indiana", "mascot": "Pacers", "league": "NBA"},
    "Los Angeles Clippers": {"city": "Los Angeles", "mascot": "Clippers", "league": "NBA"},
    "Los Angeles Lakers": {"city": "Los Angeles", "mascot": "Lakers", "league": "NBA"},
    "Memphis Grizzlies": {"city": "Memphis", "mascot": "Grizzlies", "league": "NBA"},
    "Miami Heat": {"city": "Miami", "mascot": "Heat", "league": "NBA"},
    "Milwaukee Bucks": {"city": "Milwaukee", "mascot": "Bucks", "league": "NBA"},
    "Minnesota Timberwolves": {"city": "Minnesota", "mascot": "Timberwolves", "league": "NBA"},
    "New Orleans Pelicans": {"city": "New Orleans", "mascot": "Pelicans", "league": "NBA"},
    "New York Knicks": {"city": "New York", "mascot": "Knicks", "league": "NBA"},
    "Oklahoma City Thunder": {"city": "Oklahoma City", "mascot": "Thunder", "league": "NBA"},
    "Orlando Magic": {"city": "Orlando", "mascot": "Magic", "league": "NBA"},
    "Philadelphia 76ers": {"city": "Philadelphia", "mascot": "76ers", "league": "NBA"},
    "Phoenix Suns": {"city": "Phoenix", "mascot": "Suns", "league": "NBA"},
    "Portland Trail Blazers": {"city": "Portland", "mascot": "Trail Blazers", "league": "NBA"},
    "Sacramento Kings": {"city": "Sacramento", "mascot": "Kings", "league": "NBA"},
    "San Antonio Spurs": {"city": "San Antonio", "mascot": "Spurs", "league": "NBA"},
    "Toronto Raptors": {"city": "Toronto", "mascot": "Raptors", "league": "NBA"},
    "Utah Jazz": {"city": "Utah", "mascot": "Jazz", "league": "NBA"},
    "Washington Wizards": {"city": "Washington", "mascot": "Wizards", "league": "NBA"},

    # NFL
    "Arizona Cardinals": {"city": "Arizona", "mascot": "Cardinals", "league": "NFL"},
    "Atlanta Falcons": {"city": "Atlanta", "mascot": "Falcons", "league": "NFL"},
    "Baltimore Ravens": {"city": "Baltimore", "mascot": "Ravens", "league": "NFL"},
    "Buffalo Bills": {"city": "Buffalo", "mascot": "Bills", "league": "NFL"},
    "Carolina Panthers": {"city": "Carolina", "mascot": "Panthers", "league": "NFL"},
    "Chicago Bears": {"city": "Chicago", "mascot": "Bears", "league": "NFL"},
    "Cincinnati Bengals": {"city": "Cincinnati", "mascot": "Bengals", "league": "NFL"},
    "Cleveland Browns": {"city": "Cleveland", "mascot": "Browns", "league": "NFL"},
    "Dallas Cowboys": {"city": "Dallas", "mascot": "Cowboys", "league": "NFL"},
    "Denver Broncos": {"city": "Denver", "mascot": "Broncos", "league": "NFL"},
    "Detroit Lions": {"city": "Detroit", "mascot": "Lions", "league": "NFL"},
    "Green Bay Packers": {"city": "Green Bay", "mascot": "Packers", "league": "NFL"},
    "Houston Texans": {"city": "Houston", "mascot": "Texans", "league": "NFL"},
    "Indianapolis Colts": {"city": "Indianapolis", "mascot": "Colts", "league": "NFL"},
    "Jacksonville Jaguars": {"city": "Jacksonville", "mascot": "Jaguars", "league": "NFL"},
    "Kansas City Chiefs": {"city": "Kansas City", "mascot": "Chiefs", "league": "NFL"},
    "Las Vegas Raiders": {"city": "Las Vegas", "mascot": "Raiders", "league": "NFL"},
    "Los Angeles Chargers": {"city": "Los Angeles", "mascot": "Chargers", "league": "NFL"},
    "Los Angeles Rams": {"city": "Los Angeles", "mascot": "Rams", "league": "NFL"},
    "Miami Dolphins": {"city": "Miami", "mascot": "Dolphins", "league": "NFL"},
    "Minnesota Vikings": {"city": "Minnesota", "mascot": "Vikings", "league": "NFL"},
    "New England Patriots": {"city": "New England", "mascot": "Patriots", "league": "NFL"},
    "New Orleans Saints": {"city": "New Orleans", "mascot": "Saints", "league": "NFL"},
    "New York Giants": {"city": "New York", "mascot": "Giants", "league": "NFL"},
    "New York Jets": {"city": "New York", "mascot": "Jets", "league": "NFL"},
    "Philadelphia Eagles": {"city": "Philadelphia", "mascot": "Eagles", "league": "NFL"},
    "Pittsburgh Steelers": {"city": "Pittsburgh", "mascot": "Steelers", "league": "NFL"},
    "San Francisco 49ers": {"city": "San Francisco", "mascot": "49ers", "league": "NFL"},
    "Seattle Seahawks": {"city": "Seattle", "mascot": "Seahawks", "league": "NFL"},
    "Tampa Bay Buccaneers": {"city": "Tampa Bay", "mascot": "Buccaneers", "league": "NFL"},
    "Tennessee Titans": {"city": "Tennessee", "mascot": "Titans", "league": "NFL"},
    "Washington Commanders": {"city": "Washington", "mascot": "Commanders", "league": "NFL"},
}

# -----------------------------
# Derived dictionaries
# -----------------------------

TEAM_MASCOT = {v["mascot"].lower(): k for k, v in TEAM_CANONICAL.items()}

TEAM_ABBREV = {
    # MLB
    "atl": "Atlanta Braves",
    "nyy": "New York Yankees",
    "nym": "New York Mets",
    "bos": "Boston Red Sox",
    "chc": "Chicago Cubs",
    "chw": "Chicago White Sox",
    "sf": "San Francisco Giants",
    "sd": "San Diego Padres",
    "tex": "Texas Rangers",
    # NBA
    "lal": "Los Angeles Lakers",
    "gsw": "Golden State Warriors",
    "chi": "Chicago Bulls",
    "nyk": "New York Knicks",
    # NFL
    "dal": "Dallas Cowboys",
    "sf": "San Francisco 49ers",
    "gb": "Green Bay Packers",
    "kc": "Kansas City Chiefs",
    "ne": "New England Patriots",
}

# -----------------------------
# Normalization function
# -----------------------------

def normalize_team(label: str) -> str | None:
    """Normalize CLIP/OCR team labels into canonical team names."""
    if not label:
        return None

    raw = label.strip().lower()

    # direct match
    for team in TEAM_CANONICAL:
        if raw == team.lower():
            return team

    # mascot match
    if raw in TEAM_MASCOT:
        return TEAM_MASCOT[raw]

    # abbreviation match
    if raw in TEAM_ABBREV:
        return TEAM_ABBREV[raw]

    return None

# -----------------------------
# Accessors
# -----------------------------

def get_teams():
    return TEAM_CANONICAL

def get_team_mascots():
    return TEAM_MASCOT

def get_team_abbrevs():
    return TEAM_ABBREV

