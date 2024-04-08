import filekezeles as file

sorok = file.beolvas('2024.04.08/input1.txt')
#print(sorok)
print(sorok)

szamok=file.stringSzetszedoToIntList(
    sorok[1], 
    elejerol_ennyi_nem_kell=1, 
    vegerol_ennyi_nem_kell=1)
print(szamok)

