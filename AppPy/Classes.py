import random

# Dados de vida por classe
dados_vida = {
    'BARBARO': 12,
    'BARDO': 8,
    'BRUXO': 8,
    'CLERIGO': 8,
    'DRUIDA': 8,
    'FEITICEIRO': 6,
    'GUERREIRO': 10,
    'LADINO': 8,
    'MAGO': 6,
    'MONGE': 8,
    'PALADINO': 10,
    'PATRULHEIRO': 10
}

# Função para calcular a média (arredondada para cima, como na regra oficial)
def media_vida(dado):
    return (dado // 2) + 1

# Função principal de cálculo de vida
def calcular_vida(classe, nivel, modcon, metodo='media'):
    if classe not in dados_vida:
        print('Classe inválida.')
        return None

    dado = dados_vida[classe]
    vida = dado + modcon  # Vida no nível 1

    for lvl in range(2, nivel + 1):
        if metodo == 'rolagem':
            ganho = random.randint(1, dado) + modcon
        else:
            ganho = media_vida(dado) + modcon

        # Garante que o ganho de vida não seja menor que 1 por nível
        ganho = max(ganho, 1)
        vida += ganho

    return vida

# ===== Entrada dos Dados =====
classe = input('Classe: ').strip().upper()
nivel = int(input('Nível: '))
modcon = int(input('Modificador de Constituição: '))
metodo = input('Deseja calcular com "media" ou "rolagem"? ').strip().lower()

if metodo not in ['media', 'rolagem']:
    print('Método inválido. Usando "media" por padrão.')
    metodo = 'media'

# ===== Cálculo =====
vida = calcular_vida(classe, nivel, modcon, metodo)

# ===== Saída =====
if vida is not None:
    print(f'\n=== Resultado ===')
    print(f'Classe: {classe}')
    print(f'Nível: {nivel}')
    print(f'Método: {metodo.capitalize()}')
    print(f'Vida total: {vida}')
