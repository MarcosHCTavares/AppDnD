from random import randint
from time import sleep


print('=-'*20)
print('<'*15,'OS DADOS','>'*15)
print('-='*20)
while True:
    dado = int(input('Escolha quantos lados tem o dado: '))
    quantidade = int(input('Quantos dados serão jogados? '))
    sleep(0.5)
    resultados = []
    resultados.clear()
    for i in range(quantidade):
        resultados.append(randint(1, dado))
    sleep(0.7)
    print(f'O resultado da rolagem de {quantidade} dados de {dado} lados foi: {resultados}')
    r = ' '
    while r not in 'SN':
        r = str(input('Quer rolar novamente? [S/N] ')).strip().upper()[0]
        sleep(0.5)
    if r == 'N':
        print('Obrigado por jogar conosco')
        break
