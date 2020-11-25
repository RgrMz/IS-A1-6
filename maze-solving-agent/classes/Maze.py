from classes.Cell import Cell

class Maze():

    """
        Class Description:
            This class is used to represent the maze given the number of rows and columns.
    """
    
    def __init__(self, number_rows, number_columns):

        """
            Description:
                This is the constructor of the objects of this class.
            Parameters:
                self (Maze): Represents the instance of the object, the maze you are creating/working on.
                number_rows (int): Represents the number of rows of the maze.
                number_columns (int): Represents the number of columns of the maze.
        """
        
        self._rows = number_rows
        self._columns = number_columns
        self._grid = []
        for row in range(number_rows):
            aux_row = []
            for column in range(number_columns):
                aux_row.append(Cell(row, column))
            self._grid.append(aux_row)
    
    def get_grid(self):
        return self._grid
    
    def get_cell(self, position_X, position_Y):
        return self.get_grid()[position_X][position_Y]   
    
    def get_number_rows(self):
        return self._rows
    
    def get_number_columns(self):
        return self._columns 
    
    def exists_cell(self, position_X, position_Y):
        """
            Description:
                Checks if a cell position exists in the maze limits
            Parameters:
                self (Cell): Represents the instance of the object, the cell you are creating/working on.
                position_X (int): Represents the row where the cell is.
                position_Y (int): Represents the column where the cell is.
        """
        return position_X >= 0 and position_X < len(self.get_grid()) and position_Y >= 0 and position_Y < len(self.get_grid()[0])

    def break_walls(self, cell1, cell2):

        """
            Description:
                Add a concrete neighbour to two contiguous cells.
            Parameters:
                self (Maze): Represents the instance of a Maze object.
                cell1 (Cell): Represents one cell.
                cell2 (Cell): Represents one neighbour cell of the cell1.
        """
        
        x_movement = cell1.get_X()-cell2.get_X()
        y_movement = cell1.get_Y()-cell2.get_Y()
        # As it's part of the maze
        cell1.set_in_maze()
        # VERTICAL movement
        if x_movement == -1:
            # Movement cell1 = S | Wall on cell2 = N
            cell1.add_neighbour('S')
            cell2.add_neighbour('N')
        elif x_movement == 1:
            # Movement cell1 = N | Wall on cell2 = S
            cell1.add_neighbour('N')
            cell2.add_neighbour('S')
            
        # HORIZONTAL movement
        if y_movement == -1:
            # Movement cell1 = E | Wall on cell2 = O
            cell1.add_neighbour('E')
            cell2.add_neighbour('O')
        elif y_movement == 1:
            # Movement cell1 = O | Wall on cell2 = E
            cell1.add_neighbour('O')
            cell2.add_neighbour('E')