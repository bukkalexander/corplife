
from score_data import ScoreData
from pathlib import Path
from typing import List
import json

SCORES_FILE = Path("scores.json")

def read_scores() -> List[ScoreData]:
    """Read scores from a file."""
    if not SCORES_FILE.exists():
        return []
    with open(SCORES_FILE, "r") as file:
        return json.load(file)


def write_scores(scores: List[ScoreData]):
    """Write scores to a file."""
    with SCORES_FILE.open("w") as file:
        json.dump(scores, file, indent=4)
