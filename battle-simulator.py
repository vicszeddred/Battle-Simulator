import random
import pokemon_moves

def create_pokemon_team():
    pokemon_moves.trainer_red.capture_pokemon(pokemon_moves.all_pokemon[random.randint(0, len(pokemon_moves.all_pokemon) - 1)])

def change_pokemon(pokemon_name):
    selected_pokemon = ""
    for pokemon in pokemon_moves.trainer_red.pokemon_team:
        if pokemon_name == pokemon.species:
            selected_pokemon = pokemon.species
    print("Go {pokemon}".format(selected_pokemon))

def wild_battle(difficulty):
    if difficulty.lower() == "easy":
        print("A wild {pokemon} has appeared.".format(pokemon = pokemon_moves.easy[random.randint(0, len(pokemon_moves.easy) - 1)]))
    if difficulty.lower() == "normal":
        print("A wild {pokemon} has appeared.".format(pokemon = pokemon_moves.normal[random.randint(0, len(pokemon_moves.normal) - 1)]))
    if difficulty.lower() == "hard":
        print("A wild {pokemon} has appeared.".format(pokemon = pokemon_moves.hard[random.randint(0, len(pokemon_moves.hard) - 1)]))
    print("go {mypokemon}!".format(mypokemon = pokemon_moves.trainer_red.pokemon_team[0]))
    option = input("What would you do? (battle  run) ")
    if option.lower() == "run":
        print("you have run away")
    if option.lower() == "battle":
        print("you have run away")

difficulty = input("Choose a difficulty: (easy   normal  hard) ")
create_pokemon_team()
wild_battle(difficulty)