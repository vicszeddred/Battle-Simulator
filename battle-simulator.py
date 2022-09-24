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
        if self.mtype == "Electric" or self.mtype == "Ice":
            description = "{name}, it's an {mtype}-type move."
            return description.format(name = self.name, mtype = self.mtype)
        else:
            description = "{name}, it's a {mtype}-type move."
            return description.format(name = self.name, mtype = self.mtype)

#First stage pokemon"
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

#Second stage pokemon
raichu = Pokemon("Raichu", "mouse", "Electric")
pidgeotto = Pokemon("Pidgeotto", "bird", "Normal", "Flying")
metapod = Pokemon("Metapod", "cocoon", "Bug")
kakuna = Pokemon("Kakuna", "cocoon", "Bug", "Poison")
raticate = Pokemon("Raticate", "mouse", "Normal")
nidorino = Pokemon("Nidorino", "poison pin", "Poison")
nidorina = Pokemon("Nidorina", "poison pin", "Poison")
primeape = Pokemon("Primeape", "pig monkey", "Fighthing")
ivysaur = Pokemon("Ivysaur", "seed", "grass", "Poison")
charmeleon = Pokemon("Charmeleon", "flame", "Fire")
wartotle = Pokemon("Wartotle", "turtle", "Water")

#Third stage pokemon
pidgeot = Pokemon("Pidgeot", "bird", "Normal", "Flying")
butterfree = Pokemon("Butterfree", "butterfly", "Bug", "flying")
beedrill = Pokemon("Beedrill", "poison bee", "Bug", "Poison")
nidoking = Pokemon("Nidoking", "poison pin", "Poison", "Ground")
nidoqueen = Pokemon("Nidoqueen", "poison pin", "Poison", "Ground")
venasaur = Pokemon("Venasaur", "seed", "grass", "Poison")
charizard = Pokemon("Charizard", "flame", "Fire", "Flying")
blastoise = Pokemon("Blastoise", "shellfish", "Water")

#moves
thunderShock = Move("Thunder Shock", "Electric", "Special")
vineWhip = Move("Vine Whip", "Grass", "Physical")
waterGun = Move("Water Gun", "Water", "Special")
tackle = Move("Tackle", "Normal", "Physical")
poisonSting = Move("Poison Sting", "Poison", "Physical")
bugBite = Move("Bug Bite", "Bug", "Physical")
gust = Move("Gust", "Flying", "Special")
doubleKick = Move("Double Kick", "Fighthing", "Physical")
ember = Move("Ember", "Fire", "Special")
tailWhip = Move("Tail Whip", "Normal", "Status")
growl = Move("Growl", "Normal", "Status")