# Adatok:
#   Fájlban:    Dolgozók nevei szerepelnek
#               Mellette hogy havonta mennyi palacsintát sütöttek meg

# 1) Olvasd be a fájlt megfelelő adatszerkezetbe!

filename = "input.txt"
file = open(filename, "r")
file_lista = file.readlines()
file.close

name_list = []
pancake_list = []
for i in range(len(file_lista)):
    _lista = file_lista[i].strip()
    _lista_parts = _lista.strip()
    name_list.append(_lista_parts[0])

    for j in range(1, len(_lista_parts)):
        _lista_parts[j]

    for j in range(1, len(_lista_parts)):
        _lista.append(_lista_parts[j])
    pancake_list.append(_lista)
    print(_lista_parts[0])
    print(_lista)

    for i in range(len(pancake_list)):
        print(len(pancake_list[i]))


# 2) írd ki az adatokat szépen(!!) az alábbbi fejléccel:
#       "Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"

print(file_lista)