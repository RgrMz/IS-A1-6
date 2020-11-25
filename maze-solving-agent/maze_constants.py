### Set of constants to be used along the program ###

MOVEMENTS = ['N','E','S','O']                                   ## Used in Wilson's algorithm to generate a random move
MOVE_IN_COLUMNS = {'N' : 0, 'E' : 1, 'S' : 0, 'O' : -1}         ## Used in Wilson's algorithm to move along columns
MOVE_IN_ROWS = {'N' : -1, 'E' : 0, 'S' : 1, 'O' : 0}            ## Used in Wilson's algorithm to move along rows
NEIGHBOURS_POSITION = {'N' : 0, 'E' : 1, 'S' : 2, "O" : 3}      ## Used to check the consistency of an imported JSON file
MAXIMUM_DEPTH = 1000000

### Constants to be used for drawing the maze
CELL_WIDTH = 1
BORDER_LEN = 10
CELL_WALL_LENGTH = 15

### Constants for the colors of the cells and lines
BLACK = (0,0,0)

GRASS = (152, 251, 152)
WATER = (135, 206, 250)
EARTH = (245, 222, 179)

VISITED = (0, 255, 0)
FRONTIER = (0, 0, 255)
SOLUTION = (255, 0, 0)

### Strategies to be implemented in the search algorithm

STRATEGIES = set(["BREADTH", "DEPTH", "UNIFORM", "GREEDY", "A", ])