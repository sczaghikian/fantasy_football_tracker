from typing import List

from app.draft_tracker_team import DraftTrackerTeam

class DraftTracker:
    def __init__():
        pass

    def drafted_players(drafter_list: List[DraftTrackerTeam]):
        for drafter in drafter_list:
            print(f"{drafter}")

    def drafted_players_ordered_price(drafter_list: List[DraftTrackerTeam]):
        t = []
        for drafter in drafter_list:
            t.append(drafter.roster)
        t1 = [item for sublist in t for item in sublist]
        print(" | ".join(t1.__str__))
