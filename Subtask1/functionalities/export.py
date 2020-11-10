import json
# Hide the pygame message
import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from maze_constants import *

def export_json(maze):

    """
        Description:
            Exports the internal representation of a maze to a JSON representation and save it in a JSON file
        Parameters:
            maze (Maze): Internal representation of the maze in the computer's memory
    """
    
    grid = maze.get_grid()
    
    # Creation of the dictionary
    maze_to_json = {
        "rows" : maze.get_number_rows(),
        "cols" : maze.get_number_columns(),
        "max_n" : 4,  
        "mov" : [[-1,0], [0,1], [1,0], [0,-1]],
        "id_mov" : ["N", "E", "S", "O"],
        "cells" : {},
    }
    
    # Filling the dictionary of cells 
    for row in range(maze.get_number_rows()):
        for column in range(maze.get_number_columns()):
            maze_to_json["cells"][str(maze.get_cell(row,column).get_position())] = {
                "value" : maze.get_cell(row,column).get_value(), 
                "neighbors" : maze.get_cell(row,column).get_neighbours()
            }
    
    # Saving the json file
    with open("./json-mazes/Lab_{0}_{1}.json".format(maze.get_number_rows(), maze.get_number_columns()), 'w', encoding='utf-8') as f:
        json.dump(maze_to_json, f, ensure_ascii=False, indent=2)
        
    ### A LO MEJOR INTERESA RETURNEAR EL FILENAME!!!
            
def export_image(maze):
    
    """
        Description:
            Exports the internal representation of a maze to a .png image
        Parameters:
            maze (Maze): Internal representation of the maze in the computer's memory
    """
    
    grid = maze.get_grid()
    screen_height, screen_width = cell_wall_length*maze.get_number_rows() + border_len*2, cell_wall_length*maze.get_number_columns() + border_len*2
    pygame.init()
    screen = pygame.Surface((screen_width, screen_height))
    running = True
        
    screen.fill((255,255,255))
    # Drawing all the cells
    for row in range(maze.get_number_rows()):
        for column in range(maze.get_number_columns()):
            drawCell(grid[row][column],screen, cell_wall_length, cell_wall_length)
    #You can uncomment the line below to see the image in the screen
    #pygame.display.flip()
    pygame.image.save(screen, "./images-mazes/Lab_{0}_{1}.png".format(maze.get_number_rows(), maze.get_number_columns()))

def drawCell(cell, screen, cell_x_length, cell_y_length):
    
    """
        Description:
            Draws a cell in a Surface by means of the use of pygame library
        Parameters:
            cell (Cell): Cell to be drawn
            screen (pygame.Surface): Surface where the cell is drawn
            cell_x_length (int): Starting X point where the cell is going to be drawn 
            cell_y_length (int): Starting Y point where the cell is going to be drawn
    """
    
    cell_row = cell.get_X()
    cell_column = cell.get_Y()
    north_init = [cell_x_length * cell_column + border_len, cell_y_length * cell_row + border_len]
    north_final = [cell_x_length * (cell_column + 1)  + border_len, cell_y_length * cell_row + border_len] 
    east_init = [cell_x_length * (cell_column + 1) + border_len, cell_y_length * cell_row  + border_len]
    east_final = [cell_x_length * (cell_column + 1) + border_len, cell_y_length * (cell_row + 1) + border_len]
    south_init = [cell_x_length * (cell_column + 1) + border_len, cell_y_length * (cell_row + 1) + border_len]
    south_final = [cell_x_length * cell_column + border_len, cell_y_length * (cell_row + 1) + border_len]
    west_init = [cell_x_length * cell_column + border_len, cell_y_length * (cell_row + 1) + border_len]
    west_final = [cell_x_length * cell_column + border_len, cell_y_length * cell_row + border_len]

    if cell.get_neighbours()[0] == False:
        pygame.draw.line(screen, (80, 0, 80), (north_init[0], north_init[1]), (north_final[0], north_final[1]), cell_width)
    if cell.get_neighbours()[1] == False:
        pygame.draw.line(screen, (80, 0, 80), (east_init[0], east_init[1]), (east_final[0], east_final[1]), cell_width)
    if cell.get_neighbours()[2] == False:
        pygame.draw.line(screen, (80, 0, 80), (south_init[0], south_init[1]), (south_final[0], south_final[1]), cell_width)
    if cell.get_neighbours()[3] == False:
        pygame.draw.line(screen, (80, 0, 80), (west_init[0], west_init[1]), (west_final[0], west_final[1]), cell_width)
        
def define_problem(filename):
    
    ### Later, initial state id and objective state id will
    ### be randomly generated and checked they're in the maze
    
    filename_noextension = os.path.splitext(filename)[0]
    filename_list = filename_noextension.split("_")
    problem = { "INITIAL": "(0,0)", 
               "OBJECTIVE" : "({0},{1})".format(int(filename_list[1])-1, int(filename_list[2])-1), 
               "MAZE" : filename
            }
    
    with open("./json-problems/problem_{0}_{1}.json".format(int(filename_list[1]), int(filename_list[2])), 'w', encoding='utf-8') as f:
        json.dump(problem, f, ensure_ascii=False, indent=2)