class Cell:
    def __init__(self, x: int, y: int, state: bool = False):
        self.x: int = x
        self.y: int = y
        self.some_state = state

    def toggle_state(self):
        self.some_state = not self.some_state
        
    def __str__(self):
        return f"Cell(x={self.x}, y={self.y}, state={self.some_state})"