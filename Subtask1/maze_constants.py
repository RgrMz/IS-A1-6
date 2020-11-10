### Set of constants to be used along the program ###

movements = ['N','E','S','O']                                   ## Used in Wilson's algorithm to generate a random move
move_in_columns = {'N' : 0, 'E' : 1, 'S' : 0, 'O' : -1}         ## Used in Wilson's algorithm to move along columns
move_in_rows = {'N' : -1, 'E' : 0, 'S' : 1, 'O' : 0}            ## Used in Wilson's algorithm to move along rows
neighbours_position = {'N' : 0, 'E' : 1, 'S' : 2, "O" : 3}      ## Used to check the consistency of an imported JSON file

### Constants to be used for drawing the maze
cell_width = 3
border_len = 10
cell_wall_length = 15