def successor_function (state):

    successors = []
    if state.neighbours[0]:
        successors.append(('N',state.neighbours[0],1))
    if state.neighbours[1]:
        successors.append(('E',state.neighbours[1],1))
    if state.neighbours[2]:
        successors.append(('S',state.neighbours[2],1))
    if state.neighbours[3]:
        successors.append(('O',state.neighbours[3],1))

    return successors


def goal_function(id_state, objective):
    
    return id_state == objective


def heuristic_function(candidate_row, candidate_column, target_row, target_column):
    
    # Manhattan distance Heuristic((row,column))= |row-target_row| + |column-target_column|
    return abs(candidate_row - target_row) + abs(candidate_column - target_column)

