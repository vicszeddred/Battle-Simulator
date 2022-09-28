import random
import pokemon_moves

def create_pokemon_team():
    count = 0
    while count <= 6:
        pokemon_moves.trainer_red.capture_pokemon(pokemon_moves.all_pokemon[random.randint(0, len(pokemon_moves.all_pokemon) - 1)])
        count += 1

def wild_battle(difficulty):
    if difficulty.lower() == "easy":
        print("A wild {pokemon} has appeared.".format(pokemon = pokemon_moves.easy[random.randint(0, len(pokemon_moves.easy) - 1)]))
    if difficulty.lower() == "normal":
        print("A wild {pokemon} has appeared.".format(pokemon = pokemon_moves.normal[random.randint(0, len(pokemon_moves.normal) - 1)]))
    if difficulty.lower() == "hard":
        print("A wild {pokemon} has appeared.".format(pokemon = pokemon_moves.hard[random.randint(0, len(pokemon_moves.hard) - 1)]))
    print("go {mypokemon}!".format(mypokemon = pokemon_moves.trainer_red.pokemon_team[0]))
    option = input("What would you do? (battle  pokemon     run) ")
    if option.lower() == "run":
        print("you have run away")

difficulty = input("Choose a difficulty: (easy   normal  hard) ")
create_pokemon_team()
wild_battle(difficulty)