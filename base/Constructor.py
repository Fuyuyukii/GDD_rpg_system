class constructor:
    def __init__(self, uc):
        self.class_objects: dict[str, object] = {}
        self.uc = uc

    #  Methods to object

    def add(self):
        key = self.uc(self.uc.set_id())
        self.class_objects[self.uc.set_id()] = key
        self.uc.update_id()

    # Magic Methods to improve the class

    def __getattr__(self, item):
        return self.class_objects[item]
