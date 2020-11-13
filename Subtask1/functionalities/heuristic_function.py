def heuristic_function(candidate_row, candidate_column, target_row, target_column):
    # Manhattan distance Heuristic((row,column))= |row-target_row| + |column-target_column|
    return abs(candidate_row - target_row) + abs(candidate_column - target_column)