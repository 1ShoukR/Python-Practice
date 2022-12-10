class WorldCup:
    def __init__(self, teams = None, location = None, bracket_standing = None):
        self.teams = teams
        self.location = location
        self.bracket_standing = bracket_standing
    def __str__(self):
        return f"World Cup Details: {self.teams}, {self.location}, {self.bracket_standing}"




# world_cup_games = WorldCup(teams="France vs England", location="Qatar", bracket_standing="Quarter Finals")

# print(world_cup_games)






class YourBet(WorldCup):
    def __init__(self, person_bet):
        self.person_bet = person_bet
        self.update_bet = WorldCup()
    def __str__(self):
        return f"Your bet is: {self.person_bet}. Your World Cup Details: {self.update_bet.teams}, {self.update_bet.location}, {self.update_bet.bracket_standing}"
    def update_worldcup(self, teams, location, bracket_standing):
        self.update_bet.teams = teams
        self.update_bet.location = location
        self.update_bet.bracket_standing = bracket_standing

your_bet = YourBet(person_bet="France WIN $200,000")
your_bet.update_worldcup(teams="France vs Morocco", location="Qatar", bracket_standing="semi finals")

# print(your_bet)




class Player:
    def __init__(self, first_name = None, last_name = None, email = None, password = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    def __str__(self):
        return f"Account created: {self.first_name}, {self.last_name}, {self.email}, {self.password}"



class PlayerRoll(Player):
    def __init__(self, duelist, controller, initiator, sentinel):
        self.duelist = duelist
        self.controller = controller
        self.initiator = initiator
        self.sentinel = sentinel