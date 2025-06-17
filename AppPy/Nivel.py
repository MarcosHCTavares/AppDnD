nivel = int(input('Nível: '))

if 1 <= nivel <= 4:
    bp = 2
elif 5 <= nivel <= 8:
    bp = 3
elif 9 <= nivel <= 12:
    bp = 4
elif 13 <= nivel <= 16:
    bp = 5
elif 17 <= nivel <= 20:
    bp = 6
else:
    print('Nível inválido. Insira um nível entre 1 e 20.')
    bp = None

if bp is not None:
    print(f'Bônus de Proficiência: {bp}')
