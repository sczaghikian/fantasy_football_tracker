class Player:
    """
    Represents an NFL player by name, team, position, and auction price
    """
    def __init__(
        self,
        name: str,
        team: str,
        position: str,
        purchase_price: int,
    ):
        self.name = name
        self.team = team
        self.position = position
        self.purchase_price = purchase_price
    
    def __repr__(self) -> str:
        return f"{self.name}, {self.team}, {self.position}, {self.purchase_price}"

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of this instance
        """
        return {
            "name": self.name,
            "team": self.team,
            "position": self.position,
            "purchase_price": self.purchase_price
        }
