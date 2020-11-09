from classes.Cell import Cell

# We might consider to pass the maze to the constructor in order
# to made the neighbours list of State objects, to have them in the
# successors list returned by successor function

class State():
        
    def __init__(self, cell):
        
        self.neighbours = []
        self.id = cell.get_position()
        self.value = cell.get_value()
        
        if cell.get_neighbours()[0]:
            self.neighbours.append(cell.get_North())
        else:
            self.neighbours.append(None)
        # East
        if cell.get_neighbours()[1]:
            self.neighbours.append(cell.get_East())
        else:
            self.neighbours.append(None)
        # South
        if cell.get_neighbours()[2]:
            self.neighbours.append(cell.get_South())
        else:
            self.neighbours.append(None)
        # West
        if cell.get_neighbours()[3]:
            self.neighbours.append(cell.get_West())
        else:
            self.neighbours.append(None)
        