from tst4 import Weapons


class Arsenal:
    weapons: dict[str, Weapons] = {}

    def __init__(self, n_weapons: int = 1):
        for _ in range(n_weapons):
            w = Weapons(Weapons.get_id())
            Arsenal.weapons[Weapons.get_id()] = w
            Weapons.update_id()

    def __getattr__(self, item):
        return self.weapons[item]

    @staticmethod
    def generate_more(qnt):
        for _ in range(qnt):
            w = Weapons(Weapons.get_id())
            Arsenal.weapons[Weapons.get_id()] = w
            Weapons.update_id()


arsenal = Arsenal()
