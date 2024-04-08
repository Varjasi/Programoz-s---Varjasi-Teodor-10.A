import filekezeles as file

sorok = file.beolvas('2024.04.08/input2.txt')
#print(sorok)

szamok=file.stringSzetszedoToIntList(
    sorok, 
    elejerol_ennyi_nem_kell=1, 
    vegerol_ennyi_nem_kell=1,
    adatseparator=" ")
print(szamok)

