class Weapons:
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    code_class = ""
    current_letter = 0
    id_complement = 0

    def __init__(self):
        pass

    #  Methods to Class

    @classmethod
    def update_id(cls):
        if cls.id_complement == 100:
            cls.current_letter += 1
            cls.id_complement = 0
        else:
            cls.id_complement += 1

    @classmethod
    def get_id(cls):
        return str(cls.code_class) + cls.letters[cls.current_letter] + str(cls.id_complement)

    # Getters and Setters

    @property
    def id(self):
        return self.__id


class Player(Weapons):
    code_class = "PJ"
    current_letter = 0
    id_complement = 0

    def __init__(self, idd):
        super().__init__()
        self.idd = idd
        self.player_name = ""

    @classmethod
    def get_id(cls):
        return str(cls.code_class) + cls.letters[cls.current_letter] + str(cls.id_complement)


class Player_Creator:
    players: dict[str, Player] = {}

    def __init__(self):
        p = Player(Player.get_id())
        players[Player.get_id()] = p
        Player.update_id()
