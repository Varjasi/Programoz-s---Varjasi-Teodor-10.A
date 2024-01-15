'''
x = 3
if x == 3:
    print("Az x értéke: 3")

x = 5
feltetel = True
while feltetel:
    print("cilusmag")
    if (x==7):
        feltetel = False
    x += 1
print(x)

a = input("Add meg 0")
i = 1
while a != '':
    print("Valami",i)
    a = input("Add meg 0")
    i += 1
print(f'A program kiírta összesen: {i}-szer')
'''
'''
while not True:
    pass
    '''

for i in range (10):
    pass #0-9-ig ír ki számokat

for i in range (2,5):
    pass #2,3,4

# break: megszakítja a cikuls futását
# continue: újra a ciklus feltételhez ugrik
'''
x = "szia"
for i in x:
    print(i)

x = 5
while x<10:
    pass
else:
    print("Nem lépett a ciklusba")

ijk = 7
for ijk in range(10,12):
    print(ijk)
else:
    print(f'else ág, {ijk}')
    

x = 3
y = 6
print(x>y)
print(not(x>y))
print(not(x<=y))

print(True and True) #Igaz lesz
print (True and False) #Hamis lesz

print(True and False and True) #Hamis lesz

print (True or False or True) #Igaz lesz


print (1 and 0) 
print(1 and 1)
print( (1 and 1) and (1 and 0) ) #Hamis lesz
'''
print ( (1 or 0) or (0 or 0) ) #Igaz lesz (Igaz - Hamis = Igaz)
print ( (0 or 0) or (0 or 0)) #Hamis lesz (Hamis - Hamis = Hamis)
print( (1 or 1) or (1 or 1) ) #Igaz lesz (Igaz- Igaz = Igaz)

#XOR
print (3 & 2) #Bitenként nézni meg a számokat és "és"-eli össze

# 3: 11
# 2: 10
# eredmeny: 11
print(3 | 2)

print( ~5)
# 5: 101
# ~5: 010