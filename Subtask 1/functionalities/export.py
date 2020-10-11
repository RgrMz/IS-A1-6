import json
# Hide the pygame message
import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from maze_constants import *

def export_json(maze):

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
    
    for i in range(maze.get_number_rows()):
        for j in range(maze.get_number_columns()):
            maze_to_json["cells"][str(maze.get_cell(i,j).get_position())] = {
                "value" : maze.get_cell(i,j).get_value(), 
                "neighbors" : maze.get_cell(i,j).get_neighbours()
            }
    
    # Generation of the json file
    with open("./json-mazes/Lab_{0}_{1}.json".format(maze.get_number_rows(), maze.get_number_columns()), 'w', encoding='utf-8') as f:
        json.dump(maze_to_json, f, ensure_ascii=False, indent=2)
            
def export_image(maze):
    
    grid = maze.get_grid()
    screen_height, screen_width = cell_wall_length*maze.get_number_rows() + border_len*2, cell_wall_length*maze.get_number_columns() + border_len*2
    pygame.init()
    screen = pygame.Surface((screen_width, screen_height))
    running = True
        
    screen.fill((255,255,255))
    # Drawing of all the cells
    for i in range(maze.get_number_rows()):
        for j in range(maze.get_number_columns()):
            drawCell(grid[i][j],screen, cell_wall_length, cell_wall_length)
    #pygame.display.flip()
    pygame.image.save(screen, "./images-mazes/Lab_{0}_{1}.png".format(maze.get_number_rows(), maze.get_number_columns()))

def drawCell(cell, screen, cell_x_length, cell_y_length):
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

    if cell.neighbours[0] == False:
        pygame.draw.line(screen, (80, 0, 80), (north_init[0], north_init[1]), (north_final[0], north_final[1]), cell_width)
    if cell.neighbours[1] == False:
        pygame.draw.line(screen, (80, 0, 80), (east_init[0], east_init[1]), (east_final[0], east_final[1]), cell_width)
    if cell.neighbours[2] == False:
        pygame.draw.line(screen, (80, 0, 80), (south_init[0], south_init[1]), (south_final[0], south_final[1]), cell_width)
    if cell.neighbours[3] == False:
        pygame.draw.line(screen, (80, 0, 80), (west_init[0], west_init[1]), (west_final[0], west_final[1]), cell_width)