class Plant:
    def __init__(self, species:str, location:str):
        self.species = species
        self.location = location
        print(f"Plant created: {self.species}")

class Pet:
    def __init__(self, name):
        self.name = name
        print(f"Pet created: {self.name}")

class PetPlant(Plant, Pet):
    def __init__(self, species, location, name, deco):
        super().__init__(species, location)
        Pet.__init__(self, name)
        self.deco = deco
        print(f"Pet plant: {self.name} with {self.deco}")


bob = PetPlant(
    species = "Pinus sylvestris", 
    location = "Schubert-Park", 
    name = "bob",
    deco = "scarf"
)

print(vars(bob))
print(type(bob))