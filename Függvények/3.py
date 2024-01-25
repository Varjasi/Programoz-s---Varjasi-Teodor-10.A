#Négyszetszámolás (lokális függény)
'''
def negyzet(a):
    global szam
    szam = 10
    
    return(a**3)
    

a = int(input("adj meg egy számot és kiszámolom annak a köbét \t"))
print(negyzet(a))
print(f'Globális változó: {szam}')

# a szám változó addig él ,amíg a külső függvény le nem zárva, szóval akérmennyiszer beágyazhatunk, a szám nevű változó élni fog

def kulso():
    szam = 12
    def belso():
        def belsobb():
            def legbelsobb():
                print(f'A külső függvényből: {szam}')
            legbelsobb()
        belsobb()
    belso()
kulso()

#built-in-scope (Attribútumok és metódusok megjelnítésére)

print(dir())
a = dir(__builtins__)
print(len(dir(__builtins__)))

index = 0
talalat = False

while index < len(a) and not talalat:
    if a[index] == 'map':
        talalat = True
    index +=1

if talalat:
    print(f'A map elemnek az indexe: {index-1}')
else:
    print("A listában nem található map elem!")

print(a[124])
'''

