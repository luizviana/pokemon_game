import pickle

from pessoa import *
from pokemon import *


def primeira_escolha(player):
    print("Olá {}, para começar você deve escolher um pokemon para te acompanhar nessa jornada.".format(player))
   
    pikachu = PokemonEletrico("pikachu", level=1)
    charmander = PokemonFogo("charmander", level=1)
    squirtle = PokemonAgua("squirtle", level=1)

    print("------------------------")
    print("1 - {}".format(pikachu))
    print("2 - {}".format(charmander))
    print("3 - {}".format(squirtle))
    print("------------------------")

    while True:
        escolha = input("Escolha seu pokemon: ")

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha inválida")


def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso")
    except Exception as error:
        print("Erro ao salvar o jogo")
        print(error)


def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print("Jogo carregado com sucesso")
            return player
    except Exception as error:
        print("Save não encontrado")


if __name__ == "__main__":
    print("-----------------------------------------")
    print("Bem-vindo ao game Pokemon RPG de terminal")
    print("-----------------------------------------")
    print()

    player = carregar_jogo()
    if not player:
        nome = input("Olá, qual é o seu nome: ")
        player = Player(nome)
        print("Olá {}, você acaba de adentrar num mundo habitado por pokemons.".format(nome))
        print("Sua missão é captura-los e se tornar um mestre pokemon.")
        print("mas não será tão simples, você terá que batalhar contra outros mestres de pokemons para seguir sua jornada.")
        player.mostrar_dinheiro()
        if player.pokemons:
            print("Já vi que você tem alguns pokemons")
            player.mostrar_pokemons()
        else:
            print("Você não tem nenhum pokemon. Então deve escolher um.\n")
            primeira_escolha(player)
        
        print("Pronto, agora que você possui um pokemon, enfrente seu maior inimigo, o Gary.")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua('Squirtle', level=1)])
        player.batalhar(gary)
        salvar_jogo(player)
    else:
        print("Seja bem-vindo de volta mestre pokemon")
    while True:
        print("----------------------------------------")
        print("O que deseja fazer?")
        print("1 - Explorar pelo mapa")
        print("2 - Lutar com um inimigo")
        print("3 - Mostrar pokemons")
        print("4 - Mostrar dinheiro")
        print("0 - Sair do jogo")
        escolha = input("Sua escolha: ")
        if escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == "3":
            player.mostrar_pokemons()
        elif escolha == "4":
            player.mostrar_dinheiro()
        elif escolha == "0":
            quit()
        else:
            print("Escolha inválida")