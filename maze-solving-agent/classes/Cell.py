import random

class Cell():
    
    """
        Class Description:
            This class is used to represent all the cells that are contained in the grid
            and in the final maze when found.
    """
    
    def __init__(self, row, column):
        
        """
            Description:
                This is the constructor of the objects of this class.
            Parameters:
                self (Cell): Represents the instance of the object, the cell you are creating/working on
                row (int): Represents the row it is in to set its location
                column (int): Represents the column it is in to set its location
        """
        
        self._visited = False
        self._in_maze = False
        self._neighbours = [False]*4
        self._position = (row, column)
        self._value = random.randint(0,3)   #Generates a value for: [Asphalt, Earth, Grass, Water]
    
    def is_visited(self):
        return self._visited

    def is_in_maze(self):
        return self._in_maze

    def get_position(self):
        return self._position

    def get_X(self):
        return self._position[0]
    
    def get_Y(self):
        return self._position[1]
        
    def get_neighbours(self):
        return self._neighbours
        
    def get_value(self):
        return self._value
    
    def get_visited(self):
        return self._visited
        
    def set_visited(self, state):
        self._visited = state
    
    def set_in_maze(self):
        self._in_maze = True
        
    def set_value(self, value):
        self._value = value
    
    def get_neighbours(self):
        return self._neighbours
    
    def set_neighbours(self, new_neighbours):
        self._neighbours = new_neighbours
    
    def get_North(self):
        return (self.get_X()-1, self.get_Y())
    
    def get_East(self):
        return (self.get_X(), self.get_Y()+1)
    
    def get_South(self):
        return (self.get_X()+1, self.get_Y())
    
    def get_West(self):
        return (self.get_X(), self.get_Y()-1)
    
    def add_neighbour(self, direction):
        
        """
            Description:
                This method adds a corresponding neighbour to a cell
            Parameters:
                self (Cell): Represents the instance of the object, the cell you are creating/working on
                direction (str): Represents the direction in which a neighbour has to be added
        """
        
        if direction == 'N':
            self._neighbours[0] = True
        elif direction == 'E':
            self._neighbours[1] = True
        elif direction == 'S':
            self._neighbours[2] = True
        elif direction == 'O':
            self._neighbours[3] = True