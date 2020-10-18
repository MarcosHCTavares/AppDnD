from math import floor
forca = int(input('Força '))
dex = int(input('Destreza '))
const = int(input('Constituição '))
inte = int(input('Inteligência '))
sab = int(input('Sabedoria '))
car = int(input('Carisma '))
''
modfor = (forca-10)/2
moddex = (dex-10)/2
modcon = (const-10)/2
modinte = (inte-10)/2
modsab = (sab-10)/2
modcar = (car-10)/2
''
ca = 10+moddex
''
print('\nFor {} - {}\nDex {} - {}\nConst {} - {}'
      .format(forca, floor(modfor), dex, floor(moddex), const, floor(modcon)))
print('Int {} - {}\nSab {} - {}\nCar {} - {}'
      .format(inte, floor(modinte), sab, floor(modsab), car, floor(modcar)))
print('\nClasse de Armadura {}'.format(floor(ca)))
