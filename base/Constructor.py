class constructor:
    def __init__(self, uc):
        self.class_objects: dict[str, object] = {}
        key = uc(uc.set_id())
        self.class_objects[uc.set_id()] = key
        self.uc = uc
        uc.update_id()

    #  Methods to object

    def generate_more(self, qnt):
        for _ in range(qnt):
            key = self.uc(self.uc.set_id())
            self.class_objects[self.uc.set_id()] = key
            self.uc.update_id()

    # Magic Methods to improve the class

    def __getattr__(self, item):
        return self.class_objects[item]


