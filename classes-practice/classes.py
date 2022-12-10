class WorldCup:
    def __init__(self, teams, location, bracket_standing):
        self.teams = teams
        self.location = location
        self.bracket_standing = bracket_standing
    def __str__(self):
        return f"World Cup Details: "