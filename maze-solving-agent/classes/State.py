from classes.Cell import Cell

class State():
    
    """
        Class Description:
            This class is used to represent a state, which contains an identifier (id) as the position
            of the cell it represents, as well as the value and its neighbours. It is used for problem
            solving.
    """
        
    def __init__(self, cell):

        self.neighbours = []
        self.id = cell.get_position()
        self.value = cell.get_value()
        
        #  NORTH
        #  If the cell represented by the state has the first position of its list neighbours, 
        #  which represents the neighbour on its north, it will append to the neighbours of the
        #  state de position of the cell on its north calling the method get_North() of the cell 
        #  object. If not it will append a "None".
        if cell.get_neighbours()[0]:
            self.neighbours.append(cell.get_North())
        else:
            self.neighbours.append(None)
        #  EAST
        #  If the cell represented by the state has the first position of its list neighbours, 
        #  which represents the neighbour on its east, it will append to the neighbours of the
        #  state de position of the cell on its east calling the method get_East() of the cell 
        #  object. If not it will append a "None".
        if cell.get_neighbours()[1]:
            self.neighbours.append(cell.get_East())
        else:
            self.neighbours.append(None)
        #  SOUTH
        #  If the cell represented by the state has the first position of its list neighbours, 
        #  which represents the neighbour on its south, it will append to the neighbours of the
        #  state de position of the cell on its south calling the method get_South() of the cell 
        #  object. If not it will append a "None".
        if cell.get_neighbours()[2]:
            self.neighbours.append(cell.get_South())
        else:
            self.neighbours.append(None)
        #  WEST
        #  If the cell represented by the state has the first position of its list neighbours, 
        #  which represents the neighbour on its west, it will append to the neighbours of the
        #  state de position of the cell on its west calling the method get_West() of the cell 
        #  object. If not it will append a "None".
        if cell.get_neighbours()[3]:
            self.neighbours.append(cell.get_West())
        else:
            self.neighbours.append(None)
        