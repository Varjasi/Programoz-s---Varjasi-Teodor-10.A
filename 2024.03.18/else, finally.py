
munkanapok = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']

try:
    hanyadik = int(input('Hányadik munkanapot adjam meg? '))
    munkanap = munkanapok[hanyadik - 1]
except ValueError:
    print('Nem számot adtál meg!')
except IndexError:
    print('1-5 közötti számot adhatsz csak meg!')
else:
    print(f'A {hanyadik}. munkanap a {munkanap}.')
  