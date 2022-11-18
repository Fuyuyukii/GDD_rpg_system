class Person:
    @property
    def identifier(self):
        for identifier, obj in globals().items():
            print(identifier, obj)
            if obj == self:
                return identifier


b = Person()
b.identifier
