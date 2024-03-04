"""
1. Fájl átnevezése: osztály_név.py

Feladatok:
1. A beolvas fv-ben valósítsd meg, hogy a paraméterben megadott fájlt beolvassa, és térjen vissza a szám listával az átalakítások után
2. A feladat1,2 stb fv-ben valósítsd meg a kért eljárásokat! A fájl beolvasásához használd a beolvas() függvényedet!
3. feladat1(): számold ki a fájlokban található számok összegét a tanult prog tétel segítségével!
4. feladat2(): számold ki a fájlokban található számok átlagát a tanult prog tétel segítségével!
5. feladat3(): számold ki a fájlokban található számok minimumát a tanult prog tétel segítségével!
6. feladat4(): számold ki a fájlokban található számok maximumát a tanult prog tétel segítségével!

Input fájlok használata:
feladat1() -> input1
feladat2() -> input2
feladat3() -> input3
feladat4() -> input3

Kiírások:
feladat1: [eredmény]
feladat2: [eredmény]
feladat3: [eredmény]
feladat4: [eredmény]
A ": " után csak az eremény szerepeljen

A dolgozat python fájlját küldd el a andrasi.norbert@puskas.hu-ra az alábbi tárggyal:
[osztály][filebeolvasas1] név 
"""

'''
def beolvas():
    file = open('orai/input1.txt')
    szamok = []
    for sor in file:
        szamok.append(sor)
    file.close()
def feladat1():
    file = open('orai/input2.txt')
    szamok = []
    for sor in file:
        szamok.append(sor)
    file.close()
    összeg = 0
    for szam in szamok:
        összeg =  összeg + szam    
    return(összeg)
feladat1()

def feladat3():
    file = open('orai/input3.txt')
    szamok = []
    for sor in file:
        szamok.append(sor)
    file.close()
    minimum = szamok[0]
    for szam in szamok:
        if szam < minimum:
            minimum = szam
''' 
def feladat4():
    file = open('orai/input3.txt')
    szamok = []
    for sor in file:
        szamok.append(sor)
    file.close()
    maximum = szamok[0]
    for szam in szamok:
        if szam > maximum:
            maximum = szam
    return(maximum)

def feladat2():
    file = open('orai/input2.txt')
    szamok = []
    for sor in file:
        szamok.append(sor)
    file.close()
    #Számok átlaga
    


feladat4()



    


