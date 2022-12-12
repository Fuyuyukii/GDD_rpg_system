def keys(code):
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    current_letter = 0
    id_complement = 0
    while True:
        yield str(code) + letters[current_letter] + str(id_complement)
        if id_complement == 100:
            current_letter += 1
            id_complement = 0
        else:
            id_complement += 1


macacos = keys("PT")
pinto = keys("SEXO")
dict = {}
for i in range(3):
    dict[next(macacos)] = i
print(dict)
for i in range(3):
    dict[next(pinto)] = i
print(dict)