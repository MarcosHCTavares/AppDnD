from random import randint

while True:
    dado = int(input('Escolha quantos lados tem o dado: '))
    result = randint(1, dado)
    print(f'O dado de {dado} lados caiu em {result}')
    r = ' '
    while r not in 'SN':
        r = str(input('Quer rolar novamente? [S/N] ')).strip().upper()[0]
    if r == 'N':
        print('Obrigado por jogar conosco')
        break
