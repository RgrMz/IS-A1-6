class State():
    
    def __init__(self, cell):
        
        # self.cell = cell
        self.neighbours = take_neighbours(cell) 
        self.id = cell.get_position()
        self.value = cell.get_value()
        
    def take_neighbours(self, cell):
        
        """
            Take the neighbours encoded as boolean value and return a list of such positions
        """
        # Ver si podemos mejorarlo
        neighbours = []
        # North
        if cell.get_neighbours()[0]:
            neighbours.append(cell.get_North())
        else:
            neighbours.append(None)
        # East
        if cell.get_neighbours()[1]:
            neighbours.append(cell.get_East())
        else:
            neighbours.append(None)
        # South
        if cell.get_neighbours()[2]:
            neighbours.append(cell.get_South())
        else:
            neighbours.append(None)
        # West
        if cell.get_neighbours()[3]:
            neighbours.append(cell.get_West())
        else:
            neighbours.append(None)
            
        return neighbours

