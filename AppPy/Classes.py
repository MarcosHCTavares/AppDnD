import random
''#random nunbers v
modcon = 0
nivel = 0
''#random nunbers ^
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
