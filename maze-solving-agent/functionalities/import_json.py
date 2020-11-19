import json
from maze_constants import *
from functionalities.export import export_image
from classes.Maze import Maze
from classes.Cell import Cell
from classes.ConsistencyError import ConsistencyError

def is_consistent(cell, maze):
    
    """
        Description:
            Checks for each cell in the maze if there exists an inconsistency between its neighbours. This is done
            by getting each neighbour and checking that the boolean value in such direction is the same as the boolean
            value for its neighbour in the opposite direction.
        Parameters:
            cell (Cell): Represents a concrete cell in the maze
            maze (Maze): Internal representation of the maze in the computer's memory
        Returns:
            True if there is no incosistency between a cell and its neighbours, False otherwise
    """
    
    grid = maze.get_grid()
    up_cell = right_cell = down_cell = left_cell = None

    # Checking the existance of each neighbour, i.e, in row 0 up_cell doesn't exist
    if(cell.get_Y() - 1 >= 0):
        left_cell = grid[cell.get_X()][cell.get_Y() - 1]
    if(cell.get_Y() + 1 < len(maze.get_grid()[0])):
        right_cell = grid[cell.get_X()][cell.get_Y() + 1]
    if(cell.get_X() - 1 >= 0):
        up_cell = grid[cell.get_X() - 1][cell.get_Y()]
    if(cell.get_X() + 1 < len(maze.get_grid())):
        down_cell = grid[cell.get_X() + 1][cell.get_Y()]
    
    #If a concrete neighbour exists, check the consistency
    if up_cell:
        if(cell.get_neighbours()[NEIGHBOURS_POSITION['N']] != up_cell.get_neighbours()[NEIGHBOURS_POSITION['S']]):
            return False
    if right_cell:
        if(cell.get_neighbours()[NEIGHBOURS_POSITION['E']] != right_cell.get_neighbours()[NEIGHBOURS_POSITION['O']]):
            return False
    if down_cell:
        if(cell.get_neighbours()[NEIGHBOURS_POSITION['S']] != down_cell.get_neighbours()[NEIGHBOURS_POSITION['N']]):
            return False
    if left_cell:
        if(cell.get_neighbours()[NEIGHBOURS_POSITION['O']] != left_cell.get_neighbours()[NEIGHBOURS_POSITION['E']]):
            return False
        
    return True

def import_json(file_name, export_image = True):
    
    """
        Description:
            Generates an internal representation and an image of a maze from its JSON representation.
        Parameters:
            file_name (str): Name or path where the JSON file is in the system
    """
    
    with open(file_name) as file:
        maze_dict = json.load(file)

    imported_maze = Maze(maze_dict["rows"], maze_dict["cols"])
    
    # Getting the correct state of the cells of the JSON file imported   
    for row in range(imported_maze.get_number_rows()):
        for column in range(imported_maze.get_number_columns()):
            imported_maze.get_cell(row,column).set_neighbours(maze_dict["cells"][str(imported_maze.get_cell(row,column).get_position())]["neighbors"])
            # Get the value : implemented in the future
            imported_maze.get_cell(row,column).set_value(maze_dict["cells"][str(imported_maze.get_cell(row,column).get_position())]["value"])
    
    grid = imported_maze.get_grid()
    
    # Checking the consistency of the maze and raising an error if it is not consistent
    for row in range(imported_maze.get_number_rows()):
        for column in range(imported_maze.get_number_columns()):
            if not is_consistent(grid[row][column], imported_maze):
                raise ConsistencyError("The maze has an inconsistency", file_name, grid[row][column].get_position())
            
    if (export_image):
        # If there is no exception then we can import the image
        export_image(imported_maze)
    else:
        return imported_maze 