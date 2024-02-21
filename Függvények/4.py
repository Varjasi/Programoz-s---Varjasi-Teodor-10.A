import random


def kitalando(szam):
        return(szam)
def tipp(szam):
        szam += 1

def eltalalta (tipp, szam):
        if tipp_bekero() == kitalando():
            return(True)
        else:
            tipp(1)

def tipp_bekero():
        
        a = int(input("Gondoltam egy számra 1 és 10 között! Próbáld meg kitalálni!"))
        return(a)
print(tipp_bekero())
