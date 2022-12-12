class code_bass:
    #  Base class

    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    code_class = ""
    current_letter = 0
    id_complement = 0

    #  Methods to Class

    @classmethod
    def update_id(cls):
        if cls.id_complement == 100:
            cls.current_letter += 1
            cls.id_complement = 0
        else:
            cls.id_complement += 1

    @classmethod
    def set_id(cls):
        return str(cls.code_class) + cls.letters[cls.current_letter] + str(cls.id_complement)

    # Getters and Setters
