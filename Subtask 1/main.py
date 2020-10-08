import json
import pygame
import sys
import random
from classes.Maze import Maze

# Random seed to get the random cells
random.seed(1)

###     CONSTANTS      ###
number_rows = int(sys.argv[1])
number_columns = int(sys.argv[2])
movements = ['N','E','S','O']
move_in_X = {'N' : 0, 'E' : 1, 'S' : 0, 'O' : -1}
move_in_Y = {'N' : -1, 'E' : 0, 'S' : 1, 'O' : 0}

def calculate_path(maze):
    # Wilson's Algorithm
    # Getting the number of cells that are not in the maze
    remaining_cells = number_rows * number_columns - 1

    while remaining_cells > 0:
        
        starting_cell = maze.get_cell(random.randint(0, number_rows-1), random.randint(0, number_columns-1))
        # If the starting cell is part of the maze we dont have to find its way to the maze
        if starting_cell.is_in_maze(): continue
        # If the starting cell is not part we have to visit it and make the path to a cell of the maze
        # as the starting cell is not visited yet we visit it and add it to the visited cells list
        visited_cells = []
        starting_cell.set_visited(True) 
        visited_cells.append(starting_cell)
        # We obtain the current position of the cell
        starting_X, starting_Y = starting_cell.get_X(), starting_cell.get_Y()
        
        while True:
            # Random movement
            movement = random.choice(movements)
            new_cell_X, new_cell_Y = starting_X + move_in_X[movement], starting_Y + move_in_Y[movement]
            # Checking if the movement takes us to a cell or outside the grid
            if maze.exists_cell(new_cell_X, new_cell_Y):
                # If the cell is part of the maze we encountered a solution, therefore the path finishes
                # and we dont check if it is visited or not, we dont care, its part of the solution
                if maze.get_cell(new_cell_X, new_cell_Y).is_in_maze():
                    visited_cells.append(maze.get_cell(new_cell_X, new_cell_Y))
                    remaining_cells = remaining_cells - len(visited_cells)
                    build_path(maze, visited_cells)
                    break
                # As it exists we introduce it to the visited cells list
                # If the cell is not visited we dont have a loop and we continue with the path
                if not maze.get_cell(new_cell_X, new_cell_Y).get_visited():
                    maze.get_cell(new_cell_X, new_cell_Y).set_visited(True)
                    visited_cells.append(maze.get_cell(new_cell_X, new_cell_Y))
                    starting_X, starting_Y = new_cell_X, new_cell_Y
                # If the cell is visited we have to get another random cell to continue the path
                else:
                    # To eliminate the cells that cause the loop we pop all the cells until we 
                    # encounter the same cell again
                    while True:
                        # print(len(visited_cells))
                        # print(maze.get_cell(new_cell_X, new_cell_Y).get_position())
                        popped_cell = visited_cells.pop()
                        # print(popped_cell.get_position())
                        if maze.get_cell(new_cell_X, new_cell_Y).get_position() != popped_cell.get_position():
                            popped_cell.set_visited(False)
                        else:
                            visited_cells.append(popped_cell)
                            break

def build_path(maze, visited_cells):
    """ With this method we will build the individual paths that conform the maze """
    for index,cell in enumerate(visited_cells):
        maze.break_walls(cell, visited_cells[index+1])
        if index == len(visited_cells) - 2: break 
    
                    
def main():
    
    # Declaration of the maze
    maze = Maze(number_rows, number_columns)
    grid = maze.get_grid()

    # Randomnly assigning the first cell of the maze
    ending_cell = maze.get_cell(random.randint(0, number_rows), random.randint(0, number_columns))
    ending_cell.set_in_maze()    
    
    # Calculate the paths of the maze
    calculate_path(maze)
    print(grid[0][0].get_neighbours())
    print(grid[1][0].get_neighbours())
    print(maze.get_grid()[0][0].get_neighbours())
    
if __name__ == "__main__": 
    main()

# Checking the correct creation of the maze
# for i in range(len(grid)): 
#     for j in range(len(grid[i])):
#         print(grid[i][j].get_X(), ",", grid[i][j].get_Y())