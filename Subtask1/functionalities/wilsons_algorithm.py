import random
from maze_constants import *
from classes.Maze import Maze

# Random seed to get the random movements
random.seed()

def generate_maze(maze):
    
    """
        Description:
            By implementing the Wilson's algorithm, a internal representation of a maze is generated
        Parameters:
            maze (Maze): Internal representation of the maze in the computer's memory
    """
    
    # Getting the random cell to reach it and the number of cells that are not in the maze
    ending_cell = maze.get_cell(random.randint(0, maze.get_number_rows() - 1), random.randint(0, maze.get_number_columns() - 1))
    ending_cell.set_in_maze() 
    remaining_cells = maze.get_number_rows() * maze.get_number_columns() - 1
    
    while remaining_cells > 0:
        
        starting_cell = maze.get_cell(random.randint(0, maze.get_number_rows() - 1), random.randint(0, maze.get_number_columns() - 1))
        # If the starting cell is part of the maze we dont have to find its way to the maze
        if starting_cell.is_in_maze(): continue
        
        # As the starting cell is not par of the maze yet, we visit it and add it to the visited cells list
        visited_cells = []
        starting_cell.set_visited(True) 
        visited_cells.append(starting_cell)
        # We obtain the current position of the cell
        starting_X, starting_Y = starting_cell.get_X(), starting_cell.get_Y()
        
        while True:
            # Random movement
            movement = random.choice(movements)
            # Checking if the movement takes us to a cell or outside the grid
            next_cell_X, next_cell_Y = starting_X + move_in_columns[movement], starting_Y + move_in_rows[movement]
            
            # If the cell is part of the maze we encountered a solution, therefore the path finishes
            # and we dont check if it is visited or not
            if maze.exists_cell(next_cell_X, next_cell_Y):
                if maze.get_cell(next_cell_X, next_cell_Y).is_in_maze():
                    remaining_cells = remaining_cells - len(visited_cells) 
                    visited_cells.append(maze.get_cell(next_cell_X, next_cell_Y))
                    build_path(maze, visited_cells)
                    break
                # If the cell is not visited we dont have a loop and we continue with forming path
                if not maze.get_cell(next_cell_X, next_cell_Y).get_visited():
                    maze.get_cell(next_cell_X, next_cell_Y).set_visited(True)
                    visited_cells.append(maze.get_cell(next_cell_X, next_cell_Y))
                    starting_X, starting_Y = next_cell_X, next_cell_Y
                else:
                    # A loop has been formed 
                    while True:
                        # We pop cells in the visited list until we find the first appareance of the repeated one
                        popped_cell = visited_cells.pop()
                        if maze.get_cell(next_cell_X, next_cell_Y).get_position() != popped_cell.get_position():
                            popped_cell.set_visited(False)
                        else:
                            # When we have popped the first appareance of the repeated cell, add it again to the list
                            visited_cells.append(popped_cell)
                            starting_X, starting_Y = popped_cell.get_X(), popped_cell.get_Y()
                            break

def build_path(maze, visited_cells):
    
    """
        Description:
            Builds an individual path within the maze by taking a cell and the next one in 
            the visited_cells list
        Parameters:
            maze (Maze): Internal representation of the maze in the computer's memory
            visited_cells (list): List with the cells visited by the algorithm without loops
    """    
    
    index = 0
    while index != len(visited_cells) - 1:
        maze.break_walls(visited_cells[index],visited_cells[index+1])
        index = index + 1 