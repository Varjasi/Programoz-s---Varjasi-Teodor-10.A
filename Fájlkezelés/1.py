
with open('./adatok/kimenet.txt', 'w', encoding='utf-8') as celfajl:
    # sztringet ír a fájlba
    celfajl.write('alma, körte, eper')

     # lista elemeit írja a fájlba
    celfajl.writelines(['alma\n', 'körte\n', 'eper\n'])
    
  