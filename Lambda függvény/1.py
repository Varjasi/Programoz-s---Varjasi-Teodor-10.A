
def b_oldal(teglalap):
    return teglalap[1]

teglalapok = [[1,9], [2,3], [4,8], [5,10]]
'''
print(max(teglalapok, key=lambda teglalap: teglalap[1]))
print(min(teglalapok, key=lambda tl: tl[1]))
'''
#legkisebb kerületű téglalap kiszámítása

def b_oldal(teglalap):
    return(teglalap[1])

print(min(teglalapok, key=lambda tl: (tl[0] + tl[1]) * 2))