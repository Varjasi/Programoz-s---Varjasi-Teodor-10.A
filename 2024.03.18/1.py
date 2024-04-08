import sys
print(bool(1>3 or 1<3) and (1>3) and (1>3))
print(f"Hello, {sys.argv[1]}!")
print(sys.argv)


if len(sys.argv) < 2:
    print("Nem adtál meg file nevet!")

else:
    print("")
    filename = sys.argv[1]
    file = open(filename)
    sorok  = file.readlines()
    file.close()
    print(filename)

    for i in range(len(sorok)):
        print(sorok[i].strip())

'''
Létezik-e a fájl?
'''

letezik = False

try:
    file = open(filename)

except:
    print("A fájl nem létezik")
    letezikfajl = False
