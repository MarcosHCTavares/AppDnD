atributos = {
    'Força': 0,
    'Destreza': 0,
    'Constituição': 0,
    'Inteligência': 0,
    'Sabedoria': 0,
    'Carisma': 0
}

# Coleta os valores de forma dinâmica
for atributo in atributos:
    while True:
        try:
            atributos[atributo] = int(input(f"{atributo}: "))
            break
        except ValueError:
            print("Digite um número válido!")

# Calcula modificadores (arredondamento para baixo)
modificadores = {
    nome: (valor - 10) // 2
    for nome, valor in atributos.items()
}

# Classe de Armadura (CA)
ca = 10 + modificadores['Destreza']

# Exibe resultados
print("\nAtributos e Modificadores:")
for nome, valor in atributos.items():
    print(f"{nome[:4]} {valor} - {modificadores[nome]}")

print(f"\nClasse de Armadura: {ca}")
