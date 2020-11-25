def successor_function (problem, state):

    """
        Description:
            Returns a list of the successors of a particular State, which are mapped from the available neighbours
            of a Cell in a maze.
        Parameters:
            problem (Problem): Representation of the problem
            state (State): the state which successors are to be identified
    """
    
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
    
    """
        Description:
            Returns if a concrete state is the final state (solution) of the problem or not
        Parameters:
            id_state (tuple): the id of the state to determine if it's a solution
            objective (tuple): the objective state of the problem
    """
    
    return id_state == objective


def heuristic_function(candidate_row, candidate_column, target_row, target_column):
    
    """
        Description:
            Function which implements the Manhattan distance as the heuristic used to find a solution.
        Parameters:
            candidate_row (int): the integer that represents the row of the candidate
            candidate_column (int): the integer that represents the column of the candidate
            target_row (int): the integer that represents the row of the target/objective
            target_column (int): the integer that represents the column of the target/objective
    """
    
    # Manhattan distance Heuristic((row,column))= |row-target_row| + |column-target_column|
    return abs(candidate_row - target_row) + abs(candidate_column - target_column)
