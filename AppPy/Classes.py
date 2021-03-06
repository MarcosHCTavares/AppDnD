import random
#random nunbers v
modcon = 0
nivel = 0
#random nunbers ^
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
