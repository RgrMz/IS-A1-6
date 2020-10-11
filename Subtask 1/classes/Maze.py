from classes.Cell import Cell

class Maze():
    
    def __init__(self, number_rows, number_columns):
        
        self.rows = number_rows
        self.columns = number_columns
        self.grid = []
        for row in range(number_rows):
            aux_row = []
            for column in range(number_columns):
                aux_row.append(Cell(row, column))
            self.grid.append(aux_row)
    
    def get_grid(self):
        return self.grid
    
    def get_cell(self, position_X, position_Y):
        return self.get_grid()[position_X][position_Y]    
    
    def exists_cell(self, position_X, position_Y):
        return position_X >= 0 and position_X < len(self.get_grid()) and position_Y >= 0 and position_Y < len(self.get_grid()[0])
    ## change ##
    def get_number_rows(self):
        return self.rows
    
    def get_number_columns(self):
        return self.columns
    ##change ##

    def break_walls(self, cell1, cell2):
        x_movement = cell1.get_X()-cell2.get_X()
        y_movement = cell1.get_Y()-cell2.get_Y()
        # c1 = self.get_cell(cell1.get_X(), cell1.get_Y())
        # c2 = self.get_cell(cell2.get_X(), cell2.get_Y())
        # As they are part of the maze
        cell1.set_in_maze()
        # VERTICAL movement as the X is not the same
        if x_movement == -1:
            # Movement cell1 = S | Wall on cell2 = N
            cell1.add_neighbour('S')
            cell2.add_neighbour('N')
        elif x_movement == 1:
            # Movement cell1 = N | Wall on cell2 = S
            cell1.add_neighbour('N')
            cell2.add_neighbour('S')
            
        # HORIZONTAL movement as the Y is not the same
        if y_movement == -1:
            # Movement cell1 = E | Wall on cell2 = O
            cell1.add_neighbour('E')
            cell2.add_neighbour('O')
        elif y_movement == 1:
            # Movement cell1 = O | Wall on cell2 = E
            cell1.add_neighbour('O')
            cell2.add_neighbour('E')