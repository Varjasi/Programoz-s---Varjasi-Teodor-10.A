import json

with open('JSON/adatok.json', encoding='utf-8') as diak_adatok:
    adatok = json.load(diak_adatok)

print(type(adatok))
for diak in adatok['diakok']:
    print(diak)    
  