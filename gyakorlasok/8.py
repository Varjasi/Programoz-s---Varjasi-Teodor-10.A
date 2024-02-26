#2. feladat

szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
darab = 0
for szo in szavak:
    for betu in szo:
        print(betu)
        if betu == 'a' or betu == 'A':
            darab += 1