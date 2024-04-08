def beolvas(filename:str)->list[int]:
    file= open(filename)
    sorok= file.readlines()
    file.close()
    return sorok

def strListToIntList(sorok, elsosor:int=0, a_vegerol_ennyi_sor_nem_kell:int=0)->list[int]:
    szamok=[]
    for i in range(elsosor,len(sorok)-a_vegerol_ennyi_sor_nem_kell):
        szamok.append(sorok[i].strip())
    return szamok

def stringSzetszedoToIntList(
        szoveg:str,
        separator=" ",
        elejerol_ennyi_nem_kell=0,
        vegerol_ennyi_nem_kell=0,
        adatseparator=None):
    
    egysor=szoveg.split(separator)
    if adatseparator is not None:
        egysor=egysor[
            elejerol_ennyi_nem_kell
            :len(egysor)-vegerol_ennyi_nem_kell
            ][0].split(adatseparator)
    szamok=strListToIntList(egysor)
    return szamok