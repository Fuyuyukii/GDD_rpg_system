class Weapons:
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    current_letter = 0
    id_complement = 0

    def __init__(self, id):
        self.__id = id
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
        return "W" + cls.letters[cls.current_letter] + str(cls.id_complement)

    # Getters and Setters

    @property
    def id(self):
        return self.__id


class Arsenal:
    def __init__(self, nweapons: int = 1):
        self.weapons: dict[str, Weapons] = {}

        for _ in range(nweapons):
            w = Weapons(Weapons.get_id())
            self.weapons[w.get_id()] = w
            Weapons.update_id()

    def __getattr__(self, item):
        return self.weapons[item]
