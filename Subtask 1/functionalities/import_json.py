import json
from maze_constants import *
from classes.Maze import Maze
from classes.Cell import Cell

def import_json(file_name):
    with open(file_name) as file:
        maze_dict = json.load(file)
    
    print(type(maze_string))
    imported_maze = Maze(maze_dict["rows"], maze_dict["cols"], grid) 
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(is_consistent(grid[i][j], maze) == False):
                print("Ay la reputa madre que no se dio la consistensia")