from base.Code_bass import code_bass


class party(code_bass):
    code_class = "PT"
    current_letter = 0
    id_complement = 0

    def __init__(self, id,  name: str = 'Without names'):
        self.__id = id
        self.members = list()
        self.name = name

    # General Methods

    # Methods to object

    def list_members(self):
        i = 0
        for player in self.members:
            print(f"{i + 1} - {player.name}")

    # Getters and Setters

    @property
    def party_name(self):
        return self.name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    # Magic Methods to improve the class

    def __getitem__(self, item):
        return self.members[item]

    def __len__(self):
        return len(self.members)
