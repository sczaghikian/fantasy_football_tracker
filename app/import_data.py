import json
from typing import List

from app.draft_tracker_team import DraftTrackerTeam
from app.player import Player

# TODO: make a class, make this import a whole draft

def read_draft_data(
    file_path: str
) -> List[DraftTrackerTeam]:
    """
    Reads a JSON file, creating and returning a list of DraftTracker instances

    Args:
        file_path: path to read file
    """
    with open(file_path, "r") as f:
        t = json.load(f)
    drafter_list = []
    for drafter in t:
        player_list = []
        for k, v in drafter.items():
            for player_data in v:
                player = Player(
                    player_data["name"],
                    player_data["team"],
                    player_data["position"],
                    player_data["purchase_price"]
                )
                player_list.append(player)
        drafter_list.append(DraftTrackerTeam(k, roster=player_list))
    return drafter_list