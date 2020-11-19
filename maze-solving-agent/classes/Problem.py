from classes.State import State
from classes.Cell import Cell

class Problem():
    
    def __init__(self, maze, initialState, targetState):
        
        self.maze = maze
        self.initialState = initialState
        self.finalState = targetState
        self.stateSpace = dict()
        for row in maze.get_grid():
            for cell in row:
                state = State(cell)
                self.stateSpace.update({state.id: state})
        