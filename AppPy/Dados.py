from random import randint
d2 = 0
d4 = 0
d6 = 0
d8 = 0
d10 = 0
d12 = 0
d20 = 0
d100 = 0
r = 'S'
while r == 'S':
    dado = str(input('Escolha um dado:\n[d2]\n[d4]\n[d6]\n[d8]\n[d10]\n[d12]\n[d20]\n[d100]\n')).strip().lower()
    if dado == 'd2':
        d2 = randint(1, 2)
        print(d2)
    elif dado == 'd4':
        d4 = randint(1, 4)
        print(d4)
    elif dado == 'd6':
        d6 = randint(1, 6)
        print(d6)
    elif dado == 'd8':
        d8 = randint(1, 8)
        print(d8)
    elif dado == 'd10':
        d10 = randint(1, 10)
        print(d10)
    elif dado == 'd12':
        d12 = randint(1, 12)
        print(d12)
    elif dado == 'd20':
        d20 = randint(1, 20)
        print(d20)
    elif dado == 'd100':
        d100 = randint(1, 100)
        print(d100)
    else:
        print('Não temos esse dado')
    r = str(input('Quer rolar novamente? [S/N] ')).strip().upper()
