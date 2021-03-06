import random
import math
''
while True:
    dado = int(input('Escolha quantos lados tem o dado: '))
    result = random.randint(1, dado)
    print(f'O dado de {dado} lados caiu em {result}')
    r = ' '
    while r not in 'SN':
        r = str(input('Quer rolar novamente? [S/N] ')).strip().upper()[0]
    if r == 'N':
        print('Obrigado por jogar conosco')
        break
''
nome = input('Nome')
idade = input('Idade')
peso = input('Peso')
player = input('Nome do jogador')
tendencia = input('Tendencia')
raca = str(input('Raça: '))
olhos = input('Olhos')
altura = input('Altura')
pele = input('Pele')
cabelo = input('Cabelo')
''
forca = int(input('Força '))
dex = int(input('Destreza '))
const = int(input('Constituição '))
inte = int(input('Inteligência '))
sab = int(input('Sabedoria '))
car = int(input('Carisma '))
vida = 0
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
      .format(forca, math.floor(modfor), dex, math.floor(moddex), const, math.floor(modcon)))
print('Int {} - {}\nSab {} - {}\nCar {} - {}'
      .format(inte, math.floor(modinte), sab, math.floor(modsab), car, math.floor(modcar)))
print('\nClasse de Armadura {}'.format(math.floor(ca)))
''
nivel = int(input('Nível'))
if nivel == 1:
    bonus = 2
elif nivel == 2:
    bonus = 2
elif nivel == 3:
    bonus = 2
elif nivel == 4:
    bonus = 2
elif nivel == 5:
    bonus = 3
elif nivel == 6:
    bonus = 3
elif nivel == 7:
    bonus = 3
elif nivel == 8:
    bonus = 3
elif nivel == 9:
    bonus = 4
elif nivel == 10:
    bonus = 4
elif nivel == 11:
    bonus = 4
elif nivel == 12:
    bonus = 4
elif nivel == 13:
    bonus = 5
elif nivel == 14:
    bonus = 5
elif nivel == 15:
    bonus = 5
elif nivel == 16:
    bonus = 5
elif nivel == 17:
    bonus = 6
elif nivel == 18:
    bonus = 6
elif nivel == 19:
    bonus = 6
elif nivel == 20:
    bonus = 6
''
if raca == 'Anão':
    visaoescuro = int(18)
    deslocamento = float(7.5)
    const = const + 2
elif raca == 'Anão da Montanha':
    visaoescuro = int(18)
    deslocamento = float(7.5)
    forca = forca + 2
elif raca == 'Anão da Colina':
    visaoescuro = int(18)
    deslocamento = float(7.5)
    sab = sab + 1
elif raca == 'Elfo':
    visaoescuro = int(18)
    deslocamento = float(9)
    dex = dex + 2
elif raca == 'Alto Elfo':
    visaoescuro = int(18)
    deslocamento = float(9)
    inte = inte + 1
elif raca == 'Elfo da Floresta':
    visaoescuro = int(18)
    deslocamento = float(9)
    sab = sab + 1
elif raca == 'Elfo Negro':
    visaoescuro = int(18)
    deslocamento = float(9)
    car = car + 1
elif raca == 'Halfling':
    deslocamento = float(9)
    dex = dex + 2
elif raca == 'Halfling Pés Leves':
    deslocamento = float(9)
    car = car + 1
elif raca == 'Halfling Robusto':
    deslocamento = float(9)
    const = const + 1
elif raca == 'Humano':
    deslocamento = float(9)
    forca = forca + 1
    dex = dex + 1
    const = const + 1
    inte = inte + 1
    sab = sab + 1
    car = car + 1
elif raca == 'Draconato':
    deslocamento = float(9)
    forca = forca + 2
    car = car + 1
elif raca == 'Gnomo':
    deslocamento = float(9)
    inte = inte + 2
elif raca == 'Gnomo da Floresta':
    deslocamento = float(9)
    dex = dex + 1
elif raca == 'Gnomo das Rochas':
    deslocamento = float(9)
    const = const + 1
elif raca == 'Meio-Elfo':
    visaoescuro = int(18)
    deslocamento = float(9)
    car = car + 2
elif raca == 'Meio-Orc':
    deslocamento = float(9)
    forca = forca + 2
elif raca == 'Tiefling':
    visaoescuro = int(18)
    deslocamento = float(9)
    inte = inte + 1
    car = car + 2
''
classe = str(input('Classe: '))
if classe == 'Barbáro':
    if nivel == 1:
        vida = 12 + modcon
    else:
        vida = (random.randint(1, 12) + modcon) * nivel
elif classe == 'Bardo':
    if nivel == 1:
        vida = 8 + modcon
    else:
        vida = (random.randint(1, 8) + modcon) * nivel
elif classe == 'Bruxo':
    if nivel == 1:
        vida = 8 + modcon
    else:
        vida = (random.randint(1, 8) + modcon) * nivel
elif classe == 'Clérigo':
    if nivel == 1:
        vida = 8 + modcon
    else:
        vida = (random.randint(1, 8) + modcon) * nivel
elif classe == 'Druida':
    if nivel == 1:
        vida = 8 + modcon
    else:
        vida = (random.randint(1, 8) + modcon) * nivel
elif classe == 'Feiticeiro':
    if nivel == 1:
        vida = 6 + modcon
    else:
        vida = (random.randint(1, 6) + modcon) * nivel
elif classe == 'Guerreiro':
    if nivel == 1:
        vida = 10 + modcon
    else:
        vida = (random.randint(1, 10) + modcon) * nivel
elif classe == 'Ladino':
    if nivel == 1:
        vida = 8 + modcon
    else:
        vida = (random.randint(1, 8) + modcon) * nivel
elif classe == 'Mago':
    if nivel == 1:
        vida = 6 + modcon
    else:
        vida = (random.randint(1, 6) + modcon) * nivel
elif classe == 'Monge':
    if nivel == 1:
        vida = 8 + modcon
    else:
        vida = (random.randint(1, 8) + modcon) * nivel
elif classe == 'Paladino':
    if nivel == 1:
        vida = 10 + modcon
    else:
        vida = (random.randint(1, 10) + modcon) * nivel
elif classe == 'Patrulheiro':
    if nivel == 1:
        vida = 10 + modcon
    else:
        vida = (random.randint(1, 10) + modcon) * nivel
''
print('\nNome: {}            Idade: {}            Peso: {}           Nome do jogador: {}'
      .format(nome, idade, peso, player))
print('Tendencia: {}        Olhos: {}            Altura: {}           Pele: {}           Cabelo: {}'
      .format(tendencia, olhos, altura, pele, cabelo))
print('Classe: {}           Raça: {}            Nível: {}'.format(classe, raca, nivel))
print('vida: {}'.format(vida))
