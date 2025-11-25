class Plant:
    def __init__(self, species:str, location:str):
        self.species = species
        self.location = location
        print(f"This is some sort of plant: {self.species}")
        
    def grow(self):
        print(f"The {self.species} is growing in {self.location}.")

class Pet:
    def __init__(self, name):
        self.name = name
        self.infostring = "All pets are animals that humans keep for companionship."
        print(f"This is some sort of pet: {self.name}")
        
    def play(self):
        print(f"{self.name} is playing! Look how fast {self.name} is moving!")

class PetPlant(Plant, Pet):
    def __init__(self, species, location, name, deco):
        print(f".mro() of PetPlant: {self.__class__.mro()}.")
        # This calls Plant.__init__ because Plant is the 
        # first parent class. "self" is passed automatically 
        # into the method!
        super().__init__(species, location) 
        print(f"During creation the type is already {type(self)}, even if we call super().__init__()!")
        # Now we have to call Pet.__init__ manually, because 
        # super() only called the first parent class in MRO.
        # We also have to pass "self" explicitly here!
        Pet.__init__(self, name)
        # since the infostring attribute from the pet class 
        # is not fitting my agenda, we can delete it.
        del self.infostring
        self.deco = deco
        print(f"This is a pet plant: {self.name} with {self.deco}")
        
    def play(self):
        print(f"{self.name} the plant is standing happily still!")


bob = PetPlant(
    species = "Pinus sylvestris", 
    location = "Schubert-Park", 
    name = "bob",
    deco = "scarf"
)

bob.grow()
bob.play()

# The following line shows all attributes of bob
# they are stored in bob.__dict__ which is what vars() returns.
# The function vars() is a built-in function that asks for the __dict__ 
# attribute of an object.
# The bob.__dict__ attribute is a dictionary that normally stores all attributes.
print(vars(bob))
# In fact, whenever you create an object in Python,
# you are using inheritance under the hood.
# Every class you create implicitly inherits from the base "object" class.
# Attributes like __dict__ are inherited from the base "object" class.
# Whenever you create a new class in Python, it implicitly inherits from "object".
# Eg.:
class SomeClass:
    pass
some_instance = SomeClass()
print(type(some_instance))
# is equivalent to
class SomeClass(object):
    pass
print(f".mro() of SomeClass: {SomeClass.mro()}.")
