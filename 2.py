'''
def kiir(str):
    print(str)

kiir(5)
kiir("Szia")

def összead(x, y):
    eredmeny = x + y
    print("A két szám összege: ", eredmeny)

összead(10,9)

a = 9
b = 10
összead(a,b)

def összead2(x,y,z):
    eredmeny2 = x + y + z
    print("A két szám összege :", eredmeny2)

c = 5
d = 5
e = 6
összead2(c,d,e)
'''
'''
l1 = [1,3,5,7]
l2 = [7,2,9]
l3 = [6,3,0,4]

def lista_osszeg(lista):
    sum = 0
    for i in range(len(lista)):
        sum += lista[i]
    return(sum)

a = l1
b = 0
for i in range(len(a)):
    b = b + a[i]
print(b)

c = l2
d = 0
for i in range(len(a)):
    b = b + a[i]
print(d)
'''
'''
#eljárás egyszerűen
def lista_atlag(lista):
    sum = 0
    for i in range(len(lista)):
        sum += lista[i]
    print(sum)
lista = [1,5,8]
lista_atlag(lista)

def szamok_better():
    sz1 = int(input("---"))
    sz2= int(input("---"))
    return(sz1,sz2)
'''
lista = ["alma", "citrom", "barack", "pomelo"]
print(gy[1:3]) #citrom,barack
print(gy[:]) #összes

def nagybetűs(lista):
    for i in range(len(lista)):
        lista[i]=lista[i].upper()
    return(lista)
print(lista)
print(nagybetűs(lista))
print(lista)

d1 = {}
d2=dict()
d3 = {"nev" : "doboztorta",
"szeletek" : "12"
"elfogyott: false"
}

print(d3["szeletek"])





    


