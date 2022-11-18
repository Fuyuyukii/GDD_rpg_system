class Party:
    Parties = []

    def __init__(self, name):
        self.members = list()
        self.name = name
        Party.Parties.append(name)

    def list_players(self):
        for player in self.members:
            print(player.name)


class Player:
    def __init__(self, name, party=None):
        self.name = name
        if party is not None:
            self.party = party
            self.party.members.append(self)
        else:
            self.party = None


old_monkey = Party("old_monkey")
Yuki = Player("Yuki", old_monkey)
old_monkey.list_players()
