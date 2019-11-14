import random

from pokemon import *

NOMES = [
    "Pedro",
    "Fernando",
    "Jéssica",
    "Guilherme",
    "Olivia",
    "Thalita",
    "Paulo"
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        self.pokemons = pokemons
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}".format(self.nome))
            for index,pokemon in enumerate(self.pokemons):
                print("{} - {} ({}/{})".format(index, pokemon, pokemon.ataque, pokemon.vida))
        else:
            print("{} não tem nenhum pokemon".format(self.nome))

    def mostrar_dinheiro(self):
        print("Você tem $ {} em sua carteira".format(self.dinheiro))

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Você ganhou $ {}".format(quantidade))
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        meu_pokemon = self.escolher_pokemon()

        if meu_pokemon and pokemon_inimigo:
            print("{} {}/{} vs {} {}/{}".format(meu_pokemon, meu_pokemon.ataque, meu_pokemon.vida, pokemon_inimigo, pokemon_inimigo.ataque, pokemon_inimigo.vida))
            while True:
                vitoria = meu_pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} ganhou a batalha".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * random.randint(10, 100))
                    if meu_pokemon.level < 100:
                        meu_pokemon.level += 1
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(meu_pokemon)
                if vitoria_inimiga:
                    print("{} ganhou a batalha".format(pessoa))
                    break
            meu_pokemon.vida = meu_pokemon.level * 10
            meu_pokemon.ataque = meu_pokemon.level * 5

        else:
            print("Essa batalha não pode ocorrer")
            

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self,pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("ERRO: Esse jogador não possui nenhum pokemon para ser escolhido")

    def criar_pokemons(self):
        POKEMONS = [
            PokemonFogo("Charmander"),
            PokemonFogo("Flarion"),
            PokemonFogo("Charmilion"),
            PokemonEletrico("Pikachu"),
            PokemonEletrico("Raichu"),
            PokemonAgua("Squirtle"),
            PokemonAgua("Magikarp")
        ]
        return POKEMONS


class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou um {}!".format(self.nome, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha seu pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{}: {} eu escolho você!!!".format(self,pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Escolha inválida")
        else:
            print("ERRO: Esse jogador não possui nenhum pokemon para ser escolhido")

    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(self.criar_pokemons())
            print("Um pokemon selvagem apareceu: {}".format(pokemon))

            escolha = input("Deseja tentar capturar o pokemon? (s/n)")
            if escolha == "s":
                soma_level = 0

                for i in range(len(self.pokemons)):
                    soma_level += self.pokemons[i].level
                
                media_level_pokemons = int(soma_level/len(self.pokemons))
                if random.randint(1,100) >= (pokemon.level/media_level_pokemons)/0.1:
                    self.capturar(pokemon)
                else:
                    print("{} fugiu, Que pena!!!".format(pokemon))
            elif escolha == "n":
                print("Ok, boa viagem")
            else:
                print("{} fugiu, Que pena!!!".format(pokemon))
        else:
            print("Essa exploração não deu em nada")


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(self.criar_pokemons()))
            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)

