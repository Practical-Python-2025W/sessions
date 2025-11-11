from random import random
from cell import Cell


# The following code is defining a class called World.
# The class has attributes and methods to manage a grid of Cell objects
# the __init__ method initializes the world with a configuration dictionary (you'll have to provide).
# So each world is based on the blueprint (our class) and the configuration provided.
# As you can see, the World class has methods that all take the self attribute as a first attribute.
# This is because they are instance methods that operate on the instance of the class (i.e. a concrete world) itself,
# meaning they can access and modify the instance's attributes and other methods

class World:
    """_summary_
    this class represents a world with a grid of cells and day/night cycles
    """
    def __init__(self, config: dict):
        self.config = config
        self.grid = []
        self.is_day = False
        self.width: int = config["width"]
        self.height: int = config["height"]
        self.init_grid()
    
    def tick_one_round(self):
        """_summary_
        this method simulates one round in the world, potentially altering the state of the world
        """
        # for now, this method does nothing
        pass
    
    def init_grid(self):
        """_summary_
        this method initializes the grid attribute of the World instance
        """
        # as you can see, this function creates instances of the Cell class, defined in cell.py
        self.grid = [
            [Cell(x, y) for x in range(self.width)]
            for y in range(self.height)
        ]
    
    # I didn't implement this method, but you can see how to define it
    # and what it is supposed to do from the docstring (the triple-quoted text right below the method definition)
    def get_neighboring_cells(self, cell: Cell, direction = None):
        """_summary_
        this method returns the neighbor cell of a given cell in the grid based on the specified direction
        """
        raise NotImplementedError("Upsi, this method is not yet implemented.")
    
    def toggle_day_night(self):
        """__summary_
        this method toggles the is_day attribute of the World instance
        """ 
        self.is_day = not self.is_day
    
    # this is a special method that returns a string representation of the object
    # if will be called when you use the print function on an instance of the World class
    # eg: 
    # world_instance = World({"width": 10, "height": 10})
    # print(world_instance)
    def __str__(self):
        """_summary_
        this method provides a human-readable representation of the World instance
        """
        return f"World(width={self.width}, height={self.height}, is_day={self.is_day})"

# Example usage:
# let's create an instance of the World class with a specific configuration
# calling the class like a function will use its __init__ function, we definded above
one_world_of_many = World({"width": 5, "height": 5})
# printing the world instance will invoke the __str__ method we defined above
print(one_world_of_many)
# we cpuld also directly access its attributes and methods
# for example, we can toggle the day/night state and print the world again
one_world_of_many.toggle_day_night()
# we also can mess with the attributes directly
one_world_of_many.width = 10
one_world_of_many.height = 10
# but that often isn't a good practice, better provide a method to do so 
# (for example, the grid size didn't update here, we only changed the attributes, which is highly problematic)
print(f"height: {one_world_of_many.height}, width: {one_world_of_many.width}")
# but the grid is still 5x5
print(f"Grid size: {len(one_world_of_many.grid)}x{len(one_world_of_many.grid[0])}")
# Thats bad.
# We could call the one_world_of_many.init_grid() method again to fix that, but then all current cell states would be lost.
# So we would need a better method to resize the grid while preserving cell states. But ignore that for now.
# So whatever, let's just print the world again:
print(one_world_of_many)
# Let's also print the first cell in the grid.
print(one_world_of_many.grid[0][0])
first_cell: Cell = one_world_of_many.grid[0][0]
# Since the cells in the grid are instances of the Cell class, we can use its methods.
# We could eg. toggle the state of the first cell.
first_cell.toggle_state()
# Print the first cell in the grid again to see the changed state
print(one_world_of_many.grid[0][0])

