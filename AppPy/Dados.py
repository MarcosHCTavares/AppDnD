from random import randint
from time import sleep
print('=-'*20)
print('<'*15,'OS DADOS','>'*15)
print('-='*20)
while True:
    dado = int(input('Escolha quantos lados tem o dado: '))
    sleep(0.5)
    result = randint(1, dado)
    print(f'O dado de {dado} lados caiu em {result}')
    sleep(0.7)
    r = ' '
    while r not in 'SN':
        r = str(input('Quer rolar novamente? [S/N] ')).strip().upper()[0]
        sleep(0.5)
    if r == 'N':
        print('Obrigado por jogar conosco')
        break
