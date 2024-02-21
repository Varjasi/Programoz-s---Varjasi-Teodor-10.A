'''
szamok = []



for i in range(len(sorok)):
    szam_str=sorok[i].strip()
    print(szam_str)
    szam = int(szam_str)
    szamok.append(szam)
print(szamok)

osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]
print(osszeg)

#rövidebben 

file = open('input.txt')
sorok = file.readlines()
file.close()

szamok=[]

for i in range(len(sorok)):
    szamok.append(sorok[i].strip().split(', '))
print(szamok)

'''

def beolvas(filename:str)->list[str]:
    '''
    1. Egy fájlt megnyit
    2. 
    '''
    file = open(filename)
    sorok = file.readlines()
    file.close
    return(sorok)

sorok = beolvas("13. óra/input3")
print(sorok)

import file_fvk as file

def strListToIntList feldolgozó(sorok, elsosor = 0, tobb_sor_mar_nem_kell:int = 0):
    '''
    1. elem: 
     - leveszi a felesleget
     - integerré alakítja
    '''
    szamok = []
    for i in range(elsosor,len(sorok)-tobb_sor_mar_nem_kell):
        szamok.append(int(sorok[i].strip()))
    return(szamok)

szamok = file





