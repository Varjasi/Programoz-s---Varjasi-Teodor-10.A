print('Ez a program kiszámolja az átlagodat.')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('--------------------------------------------')

darab = 0
összeg = 0

érdemjegy = int(input("Add meg az első érdemjegyedet"))

while érdemjegy != 0:
    darab = darab + 1
    összeg = összeg + érdemjegy
    érdemjegy = int(input("Add meg a következő érdemjegyedet:)"))

if érdemjegy != 0:    
    print(f'A jegyedinek az átalaga: {összeg/darab}')
else:
    print("Nem adtál meg egy érdemjegyet sem!")
