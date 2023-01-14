import json
from typing import List

from app.draft_tracker_team import DraftTrackerTeam

# TODO: make a class, make this export a whole draft

def export_draft_data(
    drafter_list: List[DraftTrackerTeam],
    file_path: str
) -> str:
    """
    Takes a list of DraftTracker classes, converts them to JSON representation, and writes the to a file

    Args:
        drafter_list: List of DraftTracker objects to store
        file_path: path to write file. Should be unique per draft
    """
    t = [dt.to_dict() for dt in drafter_list]
    print(t)
    with open(file_path, "w+") as f:
        json.dump(t, f)
    return f"Draft file successfully written to {file_path}"
