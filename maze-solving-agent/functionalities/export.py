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
    with open("./json-mazes/problem_{0}x{1}_maze.json".format(maze.get_number_rows(), maze.get_number_columns()), 'w', encoding='utf-8') as f:
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
    screen_height, screen_width = CELL_WALL_LENGTH*maze.get_number_rows() + BORDER_LEN*2, CELL_WALL_LENGTH*maze.get_number_columns() + BORDER_LEN*2
    pygame.init()
    screen = pygame.Surface((screen_width, screen_height))
    running = True
        
    screen.fill((255,255,255))
    # Drawing all the cells
    for row in range(maze.get_number_rows()):
        for column in range(maze.get_number_columns()):
            draw_cell(grid[row][column],screen)
    #You can uncomment the line below to see the image in the screen
    #pygame.display.flip()
    pygame.image.save(screen, "./images-mazes/puzzle_loop_{0}x{1}.png".format(maze.get_number_rows(), maze.get_number_columns()))

def draw_cell(cell, screen, colour = None):
    
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
    cell_value = cell.get_value()
    
    north_init = [CELL_WALL_LENGTH * cell_column + BORDER_LEN, CELL_WALL_LENGTH * cell_row + BORDER_LEN]
    north_final = [CELL_WALL_LENGTH * (cell_column + 1)  + BORDER_LEN, CELL_WALL_LENGTH * cell_row + BORDER_LEN] 
    east_init = [CELL_WALL_LENGTH * (cell_column + 1) + BORDER_LEN, CELL_WALL_LENGTH * cell_row  + BORDER_LEN]
    east_final = [CELL_WALL_LENGTH * (cell_column + 1) + BORDER_LEN, CELL_WALL_LENGTH * (cell_row + 1) + BORDER_LEN]
    south_init = [CELL_WALL_LENGTH * (cell_column + 1) + BORDER_LEN, CELL_WALL_LENGTH * (cell_row + 1) + BORDER_LEN]
    south_final = [CELL_WALL_LENGTH * cell_column + BORDER_LEN, CELL_WALL_LENGTH * (cell_row + 1) + BORDER_LEN]
    west_init = [CELL_WALL_LENGTH * cell_column + BORDER_LEN, CELL_WALL_LENGTH * (cell_row + 1) + BORDER_LEN]
    west_final = [CELL_WALL_LENGTH * cell_column + BORDER_LEN, CELL_WALL_LENGTH * cell_row + BORDER_LEN]
    
    # Variables used to color the cells
    rect_x = north_init[0] + CELL_WIDTH
    rect_y = north_init[1] + CELL_WIDTH
    rect_width = south_init[0]-south_final[0]
    rect_height = east_final[1]-east_init[1]

    # Coloring of the cells
    if cell_value != 0:
        if cell_value == 1:
            pygame.draw.rect(screen, EARTH,(rect_x, rect_y, rect_width, rect_height), 0)
        elif cell_value == 2:
            pygame.draw.rect(screen, GRASS,(rect_x, rect_y, rect_width, rect_height), 0)
        elif cell_value == 3:
            pygame.draw.rect(screen, WATER,(rect_x, rect_y, rect_width, rect_height), 0)
            
    if colour:
        pygame.draw.rect(screen, colour,(rect_x, rect_y, rect_width, rect_height), 0)
        
    if cell.get_neighbours()[0] == False:
        pygame.draw.line(screen, BLACK, (north_init[0], north_init[1]), (north_final[0], north_final[1]), CELL_WIDTH)
    if cell.get_neighbours()[1] == False:
        pygame.draw.line(screen, BLACK, (east_init[0], east_init[1]), (east_final[0], east_final[1]), CELL_WIDTH)
    if cell.get_neighbours()[2] == False:
        pygame.draw.line(screen, BLACK, (south_init[0], south_init[1]), (south_final[0], south_final[1]), CELL_WIDTH)
    if cell.get_neighbours()[3] == False:
        pygame.draw.line(screen, BLACK, (west_init[0], west_init[1]), (west_final[0], west_final[1]), CELL_WIDTH)
            
        
def define_problem(filename):
    
    filename_noextension = os.path.splitext(filename)[0]
    filename_list = filename_noextension.split("_")
    problem = { "INITIAL": "(0,0)", 
               "OBJETIVE" : "({0},{1})".format(int(filename_list[1])-1, int(filename_list[2])-1), 
               "MAZE" : filename
            }
    
    with open("./json-problems/problem_{0}x{1}.json".format(int(filename_list[1]), int(filename_list[2])), 'w', encoding='utf-8') as f:
        json.dump(problem, f, ensure_ascii=False, indent=2)
        

def save_solution(problem, nodeStack, strategy):
    
    txtSolution = '[id][cost,state,father_id,action,depth,h,value]'
    while (nodeStack):
        txtSolution += nodeStack.pop().toString()
        
    with open("./problem-solutions/solution_{0}x{1}_{2}.txt".format(problem.maze.get_number_rows(), problem.maze.get_number_columns(), strategy), 'w', encoding='utf-8' ) as f:
        f.write(txtSolution)
        
def save_solution_image(solution, frontier, visited, problem, strategy): 
    
    #Creation of the screen
    screen_height, screen_width = CELL_WALL_LENGTH*problem.maze.get_number_rows() + BORDER_LEN*2, CELL_WALL_LENGTH*problem.maze.get_number_columns() + BORDER_LEN*2
    pygame.init()
    screen = pygame.Surface((screen_width, screen_height))
    screen.fill((255,255,255))
    
    for row in range(problem.maze.get_number_rows()):
        for column in range(problem.maze.get_number_columns()):
            draw_cell(problem.maze.get_grid()[row][column],screen)
            
    while not(frontier.isEmpty()):

        node = frontier.pop()
        cell = node.idState.id
        cell_column, cell_row = cell[1], cell[0]
        
        draw_cell(problem.maze.get_cell(cell_row, cell_column), screen, FRONTIER)
        
    for cell in visited:
        
        cell_column, cell_row = cell[1], cell[0]

        draw_cell(problem.maze.get_cell(cell_row, cell_column), screen, VISITED)
        

    for node in solution:
        cell = node.idState.id
        cell_column, cell_row = cell[1], cell[0]
        
        draw_cell(problem.maze.get_cell(cell_row, cell_column), screen, SOLUTION)

    pygame.image.save(screen, "./problem-solutions/solution_{0}x{1}_{2}.png".format(problem.maze.get_number_rows(), problem.maze.get_number_columns(), strategy))
    