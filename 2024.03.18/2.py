import sys
import os 
if len(sys.argv) < 2:
    print()

elif not os.path.exists(sys.argv[1]):
    print("Ne létezik a fájl")

else:
    filename = sys.argv[1]
    file = open(filename)
    sorok = file.readlines()
    file.close()
    for i in range(len(sorok)):
        print(sorok[i])