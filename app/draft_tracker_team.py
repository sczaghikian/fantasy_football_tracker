from typing import List

from player import Player
from enums.positions import Positions

BUDGET = 200
ROSTER_SPOTS = 15


class DraftTrackerTeam:
    """
    Full draft for an individual for a year
    """
    def __init__(
        self,
        drafter: str,
        roster: List[Player]
    ):
        self.drafter = drafter
        self.roster = roster
    
    def __repr__(self) -> str:
        return f"{self.drafter}: {[[player] for player in self.roster]}"

    @property
    def remaining_budget(self):
        return BUDGET - self.spent_budget

    @property
    def spent_budget(self):
        return sum([p.purchase_price for p in self.roster])

    @property
    def TEs(self):
        return [p.name for p in self.roster if p.position == Positions.TE.value]

    @property
    def WRs(self):
        return [p.name for p in self.roster if p.position == Positions.WR.value]

    @property
    def QBs(self):
        return [p.name for p in self.roster if p.position == Positions.QB.value]

    @property
    def RBs(self):
        return [p.name for p in self.roster if p.position == Positions.RB.value]

    @property
    def DSTs(self):
        return [p.name for p in self.roster if p.position == Positions.DST.value]

    @property
    def Ks(self):
        return [p.name for p in self.roster if p.position == Positions.K.value]

    @property
    def num_players_drafted(self):
        return len(self.roster)

    @property
    def num_free_roster_spots(self):
        return ROSTER_SPOTS - self.num_players_drafted

    def add_player_to_roster(
        self,
        name: str,
        team: str,
        position: str,
        purchase_price: int
    ) -> None:
        """
        Adds an instance of the Player class to this instance's roster

        Args:
            name: player name
            team: player team
            position: player position
            purchase_price: final price paid for player in auction
        """
        p = Player(name, team, position, purchase_price)
        self.roster.append(p)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of this instance
        """
        return {
            self.drafter: [p.to_dict() for p in self.roster]
        }
