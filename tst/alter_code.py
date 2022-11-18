from base.Code_bass import code_bass


class player(code_bass):
    code_class = "PPL"
    current_letter = 0
    id_complement = 0

    def __init__(self, id, name: str = 'Without name', hp: int = 0, mp: int = 0, party=None):
        self.__id = id
        self.__name = name
        self.__lvl = 1
        self.__bag = list()
        if party is not None:
            self.party = party
            self.party.members.append(self)
        else:
            self.party = None
        self.__Mhp = hp  # Max hp
        self.__hp = hp  # Current hp
        self.__Mmp = mp  # Max mp
        self.__mp = mp  # Current mp

    # Methods to object

    def show_player(self):
        return f"Nome:{self.__name:3}\nHP:[{self.__hp:3}/{self.__Mhp:3}]\nMP:[{self.__mp}/{self.__Mmp:3}]"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp += value

    @property
    def Mhp(self):
        return self.__hp

    @Mhp.setter
    def Mhp(self, value):
        self.__hp += value

    @property
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, value):
        self.__mp += value

    @property
    def Mmp(self):
        return self.__mp

    @Mmp.setter
    def Mmp(self, value):
        self.__mp += value

    @property
    def lvl(self):
        return self.__lvl

    @lvl.setter
    def lvl(self, value):
        self.__lvl = value

    @property
    def bag(self):
        return self.__bag
