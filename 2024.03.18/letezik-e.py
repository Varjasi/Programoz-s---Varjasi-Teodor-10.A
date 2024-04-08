
'''
Létezik-e a fájl?
'''

import sys
import os
letezik = False
letezikfajl = True

try:
    file = open('input.txt')
    filename = sys.argv[1]
    print(filename)

except:
    print("A fájl nem létezik")
    letezikfajl = False

if letezikfajl:
    sorok  = file.readlines()
    file.close()
    print(file)

    for i in range(len(sorok)):
        print(sorok[i].strip())