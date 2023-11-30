#ELDÖNTÉS
# Szerepel-e hárommal oszttható szám a listában?
lista = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 1
while index < len(lista):
    if lista[index] % 3 == 0:
        talalat = True
    index += 1

print(f'A listában lévő elemek száma: {index}')
if talalat:
    print("Van a listában 3-mal osztható szám, az indexe", index-1)