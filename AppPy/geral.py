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
if nivel <= 4 :
    bp = 2
elif nivel <= 8:
    bp = 3
elif nivel <= 12:
    bp = 4
elif nivel <= 16:
    bp = 5
elif nivel <= 20:
    bp = 6
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
classe = str(input('Classe: ')).upper().strip()
if classe == 'BARBARO':
    if nivel == 1:
        vida = 12 + modcon
    else:
        vida = (random.randint(1, 12) + modcon) * nivel
elif classe == 'BARDO':
    if nivel == 1:
        vida = 8 + modcon
    else:
        vida = (random.randint(1, 8) + modcon) * nivel
elif classe == 'BRUXO':
    if nivel == 1:
        vida = 8 + modcon
    else:
        vida = (random.randint(1, 8) + modcon) * nivel
elif classe == 'CLERIGO':
    if nivel == 1:
        vida = 8 + modcon
    else:
        vida = (random.randint(1, 8) + modcon) * nivel
elif classe == 'DRUIDA':
    if nivel == 1:
        vida = 8 + modcon
    else:
        vida = (random.randint(1, 8) + modcon) * nivel
elif classe == 'FEITICEIRO':
    if nivel == 1:
        vida = 6 + modcon
    else:
        vida = (random.randint(1, 6) + modcon) * nivel
elif classe == 'GUERREIRO':
    if nivel == 1:
        vida = 10 + modcon
    else:
        vida = (random.randint(1, 10) + modcon) * nivel
elif classe == 'LADINO':
    if nivel == 1:
        vida = 8 + modcon
    else:
        vida = (random.randint(1, 8) + modcon) * nivel
elif classe == 'MAGO':
    if nivel == 1:
        vida = 6 + modcon
    else:
        vida = (random.randint(1, 6) + modcon) * nivel
elif classe == 'MONGE':
    if nivel == 1:
        vida = 8 + modcon
    else:
        vida = (random.randint(1, 8) + modcon) * nivel
elif classe == 'PALADINO':
    if nivel == 1:
        vida = 10 + modcon
    else:
        vida = (random.randint(1, 10) + modcon) * nivel
elif classe == 'PATRULHEIRO':
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
