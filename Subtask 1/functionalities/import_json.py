import json
from maze_constants import *
from functionalities.export import *
from classes.Maze import Maze
from classes.Cell import Cell
from classes.ConsistencyError import ConsistencyError

def is_consistent(cell, maze):
        
    grid = maze.get_grid()
    up_cell = right_cell = down_cell = left_cell = None

    if(cell.get_Y() - 1 >= 0):
        left_cell = grid[cell.get_X()][cell.get_Y() - 1]
    if(cell.get_Y() + 1 < len(maze.get_grid()[0])):
        right_cell = grid[cell.get_X()][cell.get_Y() + 1]
    if(cell.get_X() - 1 >= 0):
        up_cell = grid[cell.get_X() - 1][cell.get_Y()]
    if(cell.get_X() + 1 < len(maze.get_grid())):
        down_cell = grid[cell.get_X() + 1][cell.get_Y()]
    
    if up_cell:
        if(cell.get_neighbours()[neighbours_position['N']] != up_cell.get_neighbours()[neighbours_position['S']]):
            return False
    if right_cell:
        if(cell.get_neighbours()[neighbours_position['E']] != right_cell.get_neighbours()[neighbours_position['O']]):
            return False
    if down_cell:
        if(cell.get_neighbours()[neighbours_position['S']] != down_cell.get_neighbours()[neighbours_position['N']]):
            return False
    if left_cell:
        if(cell.get_neighbours()[neighbours_position['O']] != left_cell.get_neighbours()[neighbours_position['E']]):
            return False
        
    return True

def import_json(file_name):
    
    with open(file_name) as file:
        maze_dict = json.load(file)

    imported_maze = Maze(maze_dict["rows"], maze_dict["cols"])
    
    for i in range(imported_maze.get_number_rows()):
        for j in range(imported_maze.get_number_columns()):
            imported_maze.get_cell(i,j).set_neighbours(maze_dict["cells"][str(imported_maze.get_cell(i,j).get_position())]["neighbors"])
            # Get the value : FUTURE
            # imported_maze.get_cell(i,j).set_value(maze_dict["cells"][str(imported_maze.get_cell(i,j).get_position())]["value"])
    
    grid = imported_maze.get_grid()
    for i in range(imported_maze.get_number_rows()):
        for j in range(imported_maze.get_number_columns()):
            if not is_consistent(grid[i][j], imported_maze):
                raise ConsistencyError("The maze has an inconsistency", file_name, grid[i][j].get_position())
    # If there is no exception then we can import the image
    export_image(imported_maze)  