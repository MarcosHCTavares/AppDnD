# Dados raciais com visão, deslocamento, bônus, idiomas e proficiências
racas = {
    'Anão': {
        'visaoescuro': 18, 'deslocamento': 7.5, 'const': 2,
        'idiomas': ['Comum', 'Anânico'],
        'proficiencias': ['Machados de batalha', 'Machadinhas', 'Martelos leves', 'Martelos de guerra', 'Ferramentas de artesão (Escolha)']
    },
    'Anão da Montanha': {
        'visaoescuro': 18, 'deslocamento': 7.5, 'forca': 2,
        'idiomas': ['Comum', 'Anânico'],
        'proficiencias': ['Armadura leve', 'Armadura média']
    },
    'Anão da Colina': {
        'visaoescuro': 18, 'deslocamento': 7.5, 'sab': 1,
        'idiomas': ['Comum', 'Anânico'],
        'proficiencias': []
    },
    'Elfo': {
        'visaoescuro': 18, 'deslocamento': 9, 'dex': 2,
        'idiomas': ['Comum', 'Élfico'],
        'proficiencias': ['Percepção']
    },
    'Alto Elfo': {
        'visaoescuro': 18, 'deslocamento': 9, 'inte': 1,
        'idiomas': ['Comum', 'Élfico', 'Outro idioma à escolha'],
        'proficiencias': ['Espadas longas', 'Espadas curtas', 'Arcos longos', 'Arcos curtos']
    },
    'Elfo da Floresta': {
        'visaoescuro': 18, 'deslocamento': 9, 'sab': 1,
        'idiomas': ['Comum', 'Élfico'],
        'proficiencias': ['Espadas longas', 'Espadas curtas', 'Arcos longos', 'Arcos curtos']
    },
    'Elfo Negro': {
        'visaoescuro': 18, 'deslocamento': 9, 'car': 1,
        'idiomas': ['Comum', 'Élfico'],
        'proficiencias': ['Espadas longas', 'Espadas curtas', 'Arcos longos', 'Arcos curtos']
    },
    'Halfling': {
        'deslocamento': 7.5, 'dex': 2,
        'idiomas': ['Comum', 'Halfling'],
        'proficiencias': []
    },
    'Halfling Pés Leves': {
        'deslocamento': 7.5, 'car': 1,
        'idiomas': ['Comum', 'Halfling'],
        'proficiencias': []
    },
    'Halfling Robusto': {
        'deslocamento': 7.5, 'const': 1,
        'idiomas': ['Comum', 'Halfling'],
        'proficiencias': []
    },
    'Humano': {
        'deslocamento': 9, 'forca':1, 'dex':1, 'const':1, 'inte':1, 'sab':1, 'car':1,
        'idiomas': ['Comum', 'Outro idioma à escolha'],
        'proficiencias': []
    },
    'Draconato': {
        'deslocamento': 9, 'forca':2, 'car':1,
        'idiomas': ['Comum', 'Dracônico'],
        'proficiencias': []
    },
    'Gnomo': {
        'deslocamento': 7.5, 'inte':2,
        'idiomas': ['Comum', 'Gnômico'],
        'proficiencias': []
    },
    'Gnomo da Floresta': {
        'deslocamento': 7.5, 'dex':1,
        'idiomas': ['Comum', 'Gnômico'],
        'proficiencias': []
    },
    'Gnomo das Rochas': {
        'deslocamento': 7.5, 'const':1,
        'idiomas': ['Comum', 'Gnômico'],
        'proficiencias': ['Ferramentas de artesão (Engenheiro)']
    },
    'Meio-Elfo': {
        'visaoescuro': 18, 'deslocamento':9, 'car':2,
        'idiomas': ['Comum', 'Élfico', 'Outro idioma à escolha'],
        'proficiencias': ['Escolha duas perícias à sua escolha']
    },
    'Meio-Orc': {
        'deslocamento':9, 'forca':2,
        'idiomas': ['Comum', 'Orc'],
        'proficiencias': ['Intimidação']
    },
    'Tiefling': {
        'visaoescuro':18, 'deslocamento':9, 'inte':1, 'car':2,
        'idiomas': ['Comum', 'Infernal'],
        'proficiencias': []
    }
}

# Atributos base
atributos = {
    'forca': 0,
    'dex': 0,
    'const': 0,
    'inte': 0,
    'sab': 0,
    'car': 0,
    'visaoescuro': 0,
    'deslocamento': 0
}

idiomas = []
proficiencias = []

# Input de raça
raca = input('Escolha sua raça: ').strip().title()

if raca in racas:
    bonus = racas[raca]
    for chave, valor in bonus.items():
        if chave in atributos:
            atributos[chave] += valor
        elif chave == 'idiomas':
            idiomas.extend(valor)
        elif chave == 'proficiencias':
            proficiencias.extend(valor)

    # Exibir os atributos após aplicar os bônus raciais
    print('\n=== Atributos após bônus racial ===')
    for chave, valor in atributos.items():
        if valor != 0:
            print(f'{chave.capitalize()}: {valor}')

    print('\n=== Idiomas ===')
    for idioma in idiomas:
        print(f'- {idioma}')

    print('\n=== Proficiências ===')
    if proficiencias:
        for prof in proficiencias:
            print(f'- {prof}')
    else:
        print('Nenhuma proficiência racial.')

else:
    print('Raça inválida.')
