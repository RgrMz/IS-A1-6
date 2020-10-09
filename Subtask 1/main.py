import json
import pygame
import sys
import random
from classes.Maze import Maze

# Random seed to get the random cells
random.seed()

###     CONSTANTS      ###
number_rows = int(sys.argv[1])
number_columns = int(sys.argv[2])
movements = ['N','E','S','O']
move_in_columns = {'N' : 0, 'E' : 1, 'S' : 0, 'O' : -1}
move_in_rows = {'N' : -1, 'E' : 0, 'S' : 1, 'O' : 0}

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
            print(movement)
            next_cell_X, next_cell_Y = starting_X + move_in_columns[movement], starting_Y + move_in_rows[movement]
            # Checking if the movement takes us to a cell or outside the grid
            if maze.exists_cell(next_cell_X, next_cell_Y):
                # If the cell is part of the maze we encountered a solution, therefore the path finishes
                # and we dont check if it is visited or not, we dont care, its part of the solution
                if maze.get_cell(next_cell_X, next_cell_Y).is_in_maze():
                    remaining_cells = remaining_cells - len(visited_cells) 
                    visited_cells.append(maze.get_cell(next_cell_X, next_cell_Y))
                    build_path(maze, visited_cells)
                    break
                # As it exists we introduce it to the visited cells list
                # If the cell is not visited we dont have a loop and we continue with the path
                if not maze.get_cell(next_cell_X, next_cell_Y).get_visited():
                    maze.get_cell(next_cell_X, next_cell_Y).set_visited(True)
                    visited_cells.append(maze.get_cell(next_cell_X, next_cell_Y))
                    starting_X, starting_Y = next_cell_X, next_cell_Y
                # If the cell is visited we have to get another random cell to continue the path
                else:
                    # To eliminate the cells that cause the loop we pop all the cells until we 
                    # encounter the same cell again
                    while True:
                        # print(len(visited_cells))
                        popped_cell = visited_cells.pop()
                        if maze.get_cell(next_cell_X, next_cell_Y).get_position() != popped_cell.get_position():
                            popped_cell.set_visited(False)
                        else:
                            visited_cells.append(popped_cell)
                            starting_X, starting_Y = popped_cell.get_X(), popped_cell.get_Y()
                            break

def build_path(maze, visited_cells):
    """ With this method we will build the individual paths that conform the maze """
    # for index,cell in enumerate(visited_cells):
    #     maze.break_walls(cell, visited_cells[index+1])
    #     if index == len(visited_cells) - 2: break
    index = 0
    while index != len(visited_cells) - 1:
        maze.break_walls(visited_cells[index],visited_cells[index+1])
        index = index + 1
                    
def main():
    
    # Declaration of the maze
    maze = Maze(number_rows, number_columns)
    grid = maze.get_grid()

    # Randomnly assigning the first cell of the maze
    ending_cell = maze.get_cell(random.randint(0, number_rows-1), random.randint(0, number_columns-1))
    ending_cell.set_in_maze()    
    
    # Calculate the paths of the maze
    calculate_path(maze)
    for i in range(len(grid)): 
        for j in range(len(grid[i])):
            print(maze.get_grid()[i][j].get_position(), ": ", maze.get_grid()[i][j].get_neighbours())

    
if __name__ == "__main__": 
    main()

#Checking the correct creation of the maze
# for i in range(len(grid)): 
#     for j in range(len(grid[i])):
#         print(grid[i][j].get_X(), ",", grid[i][j].get_Y())
