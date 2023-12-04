# hány darab hárommal osztható szám van a listában?

lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

db = 0

for szam in lista:
    if szam % 3 == 0:
        db += 1
print(f'A listában {db} db 3-mal osztható szám található')