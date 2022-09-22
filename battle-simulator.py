class Pokemon:
    def __init__(self, species, category, type1, type2 = ""):
        self.species = species
        self.type1 = type1
        self.type2 = type2
        self.category = category

    def __repr__(self):
        description = ""
        if self.type2 != "":
            description = "{species}, the {category} Pokemon. It's {type1}/{type2}-type."
            return description.format(species = self.species, category = self.category, type1 = self.type1, type2 = self.type2)
        else:
            description = "{species}, the {category} Pokemon. It's {type1}-type."
            return description.format(species = self.species, category = self.category, type1 = self.type1)

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