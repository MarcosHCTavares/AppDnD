from random import randint
from time import sleep


def rolar_dados(lados, quantidade):
    return [randint(1, lados) for _ in range(quantidade)]


print('=-' * 20)
print('<' * 15, ' SIMULADOR DE DADOS ', '>' * 15)
print('-=' * 20)

while True:
    try:
        dado = int(input('Quantos lados tem o dado? (mínimo 2) '))
        if dado < 2:
            print('O dado precisa ter no mínimo 2 lados.')
            continue

        quantidade = int(input('Quantos dados serão jogados? (mínimo 1) '))
        if quantidade < 1:
            print('Precisa jogar pelo menos 1 dado.')
            continue

        print('\nRolando os dados...')
        sleep(1)

        resultados = rolar_dados(dado, quantidade)

        print(f'\n🎲 Resultado da rolagem de {quantidade} dado(s) de {dado} lados:')
        print(' -> ', ' | '.join(str(num) for num in resultados))

        r = input('\nQuer rolar novamente? [S/N] ').strip().upper()
        if r != 'S':
            print('\nObrigado por jogar! Até a próxima. 🎲')
            break

        print('-=' * 20)

    except ValueError:
        print('Por favor, insira apenas números válidos.')
