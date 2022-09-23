class Pokemon:
    def __init__(self, species, category, type1, type2 = ""):
        self.species = species
        self.type1 = type1
        self.type2 = type2
        self.category = category
        moves = []

    def __repr__(self):
        description = ""
        if self.type2 != "":
            description = "{species}, the {category} Pokemon. It's {type1}/{type2}-type."
            return description.format(species = self.species, category = self.category, type1 = self.type1, type2 = self.type2)
        else:
            description = "{species}, the {category} Pokemon. It's {type1}-type."
            return description.format(species = self.species, category = self.category, type1 = self.type1)
    
    def learn_move(self, move):
        if type(move) is Move:
            if len(self.moves) <= 4:
                print("1.. 2.. 3.. TA DA!")
                self.moves.append(move)
                print("{species} has learn {move}!".format(species = self.species, move = move))
            else:
                print("1.. 2.. 3.. TA DA!")
                print("{species} has forgotten {old_move} and has learn {new_move}".format(species = self.species, old_move = self.moves[-1], new_move = move))
                self.moves[-1] = move
            if move in self.moves:
                print("{species} already knows {move}.".format(species = self.species, move = move))


class Move:
    def __init__(self, name, mtype, mclass):
        self.name = name
        self.mtype = mtype
        self.mclass = mclass

    def __repr__(self):
        description = ""
        if self.type == "Electric" or self.type == "Ice":
            description = "{name}, it's an {mtype}-type move."
            return description.format(name = self.name, mtype = self.mtype)
        else:
            description = "{name}, it's a {mtype}-type move."
            return description.format(name = self.name, mtype = self.mtype)


pikachu = Pokemon("Pikachu", "electric mouse", "Electric")
pidgey = Pokemon("Pidgey", "tiny bird", "normal", "flying")
caterpie = Pokemon('Caterpie', 'worm', 'bug')
weedle = Pokemon('Weedle', 'hairy worm', 'bug', 'poison')
ratatta = Pokemon('Ratatta', 'mouse', 'normal')
nidoranM = Pokemon('Nidoran♂', 'poison pin', 'poison')
nidoranF = Pokemon('Nidoran♀', 'poison pin', 'poison')
mankey = Pokemon("Mankey", 'pig monkey', 'fighthing')
bulbasaur = Pokemon('Bulbasaur', 'seed', 'grass', 'poison')
charmander = Pokemon('Charmander', 'lizard', 'fire')
squirtle = Pokemon('Squirtle', ' tiny turtle', 'water')