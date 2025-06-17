import random
import math

# --- Funções Reutilizáveis ---
def rolar_dado():
    while True:
        try:
            lados = int(input("Escolha quantos lados tem o dado: "))
            resultado = random.randint(1, lados)
            print(f"O dado de {lados} lados caiu em {resultado}")
            
            while True:
                repetir = input("Quer rolar novamente? [S/N] ").strip().upper()
                if repetir in ("S", "N"):
                    break
                print("Digite 'S' ou 'N'.")
            
            if repetir == "N":
                print("Obrigado por jogar conosco!")
                return
        
        except ValueError:
            print("Digite um número válido!")

def calcular_modificador(atributo):
    return (atributo - 10) // 2

# --- Dados das Raças (atributos bônus, visão, deslocamento) ---
RACAS = {
    "Anão": {"const": 2, "visao": 18, "deslocamento": 7.5},
    "Anão da Montanha": {"forca": 2, "visao": 18, "deslocamento": 7.5},
    "Anão da Colina": {"sab": 1, "visao": 18, "deslocamento": 7.5},
    "Elfo": {"dex": 2, "visao": 18, "deslocamento": 9},
    "Alto Elfo": {"inte": 1, "visao": 18, "deslocamento": 9},
    "Elfo da Floresta": {"sab": 1, "visao": 18, "deslocamento": 9},
    "Elfo Negro": {"car": 1, "visao": 18, "deslocamento": 9},
    "Halfling": {"dex": 2, "deslocamento": 9},
    "Halfling Pés Leves": {"car": 1, "deslocamento": 9},
    "Halfling Robusto": {"const": 1, "deslocamento": 9},
    "Humano": {"forca": 1, "dex": 1, "const": 1, "inte": 1, "sab": 1, "car": 1, "deslocamento": 9},
    "Draconato": {"forca": 2, "car": 1, "deslocamento": 9},
    "Gnomo": {"inte": 2, "deslocamento": 9},
    "Gnomo da Floresta": {"dex": 1, "deslocamento": 9},
    "Gnomo das Rochas": {"const": 1, "deslocamento": 9},
    "Meio-Elfo": {"car": 2, "visao": 18, "deslocamento": 9},
    "Meio-Orc": {"forca": 2, "deslocamento": 9},
    "Tiefling": {"inte": 1, "car": 2, "visao": 18, "deslocamento": 9},
}

# --- Dados das Classes (dados de vida) ---
CLASSES = {
    "BARBARO": {"dado_vida": 12},
    "BARDO": {"dado_vida": 8},
    "BRUXO": {"dado_vida": 8},
    "CLERIGO": {"dado_vida": 8},
    "DRUIDA": {"dado_vida": 8},
    "FEITICEIRO": {"dado_vida": 6},
    "GUERREIRO": {"dado_vida": 10},
    "LADINO": {"dado_vida": 8},
    "MAGO": {"dado_vida": 6},
    "MONGE": {"dado_vida": 8},
    "PALADINO": {"dado_vida": 10},
    "PATRULHEIRO": {"dado_vida": 10},
}

# --- Criação do Personagem ---
def criar_personagem():
    personagem = {
        "nome": input("Nome: "),
        "idade": input("Idade: "),
        "peso": input("Peso: "),
        "jogador": input("Nome do jogador: "),
        "tendencia": input("Tendência: "),
        "olhos": input("Olhos: "),
        "altura": input("Altura: "),
        "pele": input("Pele: "),
        "cabelo": input("Cabelo: "),
    }

    # Atributos básicos
    atributos = {
        "forca": int(input("Força: ")),
        "dex": int(input("Destreza: ")),
        "const": int(input("Constituição: ")),
        "inte": int(input("Inteligência: ")),
        "sab": int(input("Sabedoria: ")),
        "car": int(input("Carisma: ")),
    }

    # Raça (aplica bônus)
    raca = input("Raça: ").strip()
    if raca in RACAS:
        for atrib, bonus in RACAS[raca].items():
            if atrib in atributos:
                atributos[atrib] += bonus
    else:
        print("Raça não reconhecida. Sem bônus aplicados.")

    # Modificadores
    modificadores = {atrib: calcular_modificador(valor) for atrib, valor in atributos.items()}
    ca = 10 + modificadores["dex"]

    # Classe e nível
    classe = input("Classe: ").upper().strip()
    nivel = int(input("Nível: "))
    bp = 2 + (nivel - 1) // 4  # Bônus de Proficiência calculado dinamicamente

    # Cálculo de vida
    if classe in CLASSES:
        dado_vida = CLASSES[classe]["dado_vida"]
        if nivel == 1:
            vida = dado_vida + modificadores["const"]
        else:
            vida = sum(random.randint(1, dado_vida) for _ in range(nivel)) + (modificadores["const"] * nivel)
    else:
        vida = 0  # Classe não reconhecida

    # Exibir ficha
    print("\n--- FICHA DO PERSONAGEM ---")
    print(f"Nome: {personagem['nome']} | Idade: {personagem['idade']} | Peso: {personagem['peso']}")
    print(f"Jogador: {personagem['jogador']} | Tendência: {personagem['tendencia']}")
    print(f"Raça: {raca} | Classe: {classe} | Nível: {nivel}")
    print(f"Olhos: {personagem['olhos']} | Altura: {personagem['altura']}")
    print(f"Pele: {personagem['pele']} | Cabelo: {personagem['cabelo']}\n")

    print("--- ATRIBUTOS ---")
    for atrib, valor in atributos.items():
        print(f"{atrib[:4].upper()} {valor} (Mod: {modificadores[atrib]})")

    print(f"\nCA: {ca} | Vida: {vida} | Bônus de Proficiência: +{bp}")

# --- Execução ---
if __name__ == "__main__":
    rolar_dado()  # Opcional: chamar primeiro para rolar dados
    criar_personagem()
