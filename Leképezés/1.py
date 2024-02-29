#Lista elemeinek átalakítása float típussá
'''
átalakított = []

szamok = ['2.5', '3.5', '4.5']

for szam in szamok:
    a = float(szam)
    átalakított.append(a)

print(átalakított)
'''

#Rövidebben 

szamok = ['2.5', '3.5', '4.5']
def átalakító():
    átalakított = [float(szam) for szam in szamok]
    print(átalakított)


átalakító()
