from classes.State import State
from classes.Cell import Cell

class Problem():
    
    """
        Class Description:
            This class is used to represent a problem, containing essential information such as
            the maze to be used, the initial state, the final state, the last ID generated for a Node
            and the whole state space for the problem.
    """
    
    def __init__(self, maze, initialState, targetState):
        
        self.maze = maze
        self.initialState = initialState
        self.finalState = targetState
        self.stateSpace = dict()
        self.lastId = 0
        for row in maze.get_grid():
            for cell in row:
                state = State(cell)
                self.stateSpace.update({state.id: state})