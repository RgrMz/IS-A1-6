def successor_function (problem, state):

# These values correspond to the 'cost' 
# of travelling through them. 
# In this way the cost of an action is set as the value of the target box + 1 (If the target box is Grass it would be 2+1=3)
    successors = []
    if state.neighbours[0]:
        successors.append(('N', state.neighbours[0], problem.stateSpace[state.neighbours[0]].value + 1))
    if state.neighbours[1]:
        successors.append(('E', state.neighbours[1], problem.stateSpace[state.neighbours[1]].value + 1))
    if state.neighbours[2]:
        successors.append(('S', state.neighbours[2], problem.stateSpace[state.neighbours[2]].value + 1))
    if state.neighbours[3]:
        successors.append(('O', state.neighbours[3], problem.stateSpace[state.neighbours[3]].value + 1))

    return successors

def goal_function(id_state, objective):
    
    return id_state == objective


def heuristic_function(candidate_row, candidate_column, target_row, target_column):
    
    # Manhattan distance Heuristic((row,column))= |row-target_row| + |column-target_column|
    return abs(candidate_row - target_row) + abs(candidate_column - target_column)
