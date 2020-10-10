class Cell():
    """ A class representing a cell in the maze"""
    neighbours = []
    def __init__(self, row, column):
        
        self.visited = False
        self.in_maze = False
        self.neighbours = [False]*4
        self.position = (row, column)
        self.value = 0
    
    def is_visited(self):
        return self.visited

    def is_in_maze(self):
        return self.in_maze

    def get_position(self):
        return self.position

    def get_X(self):
        return self.position[0]
    
    def get_Y(self):
        return self.position[1]
        
    def get_neighbours(self):
        return self.neighbours
        
    def get_value(self):
        return self.value
    
    def get_visited(self):
        return self.visited
        
    def set_visited(self, state):
        self.visited = state
    
    def set_in_maze(self):
        self.in_maze = True
    
    def get_neighbours(self):
        return self.neighbours
    
    def set_neighbours(self, new_neighbours):
        self.neighbours = new_neighbours
        
    def add_neighbour(self, direction):
        if direction == 'N':
            self.neighbours[0] = True
        elif direction == 'E':
            self.neighbours[1] = True
        elif direction == 'S':
            self.neighbours[2] = True
        elif direction == 'O':
            self.neighbours[3] = True