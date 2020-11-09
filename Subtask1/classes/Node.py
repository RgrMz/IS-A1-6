from classes.State import State

class Node():
    
    def __init__(self, idNode, cost, newState, parent, action, depth, heuristic):
        
        self.id = idNode
        self.cost = cost
        self.idState = newState
        self.idParent = parent
        self.action = action
        self.depth = depth
        self.heuristic = heuristic
        self.value = 0

    def toString (self):
        return (f"\nNode ID: {self.id} \nState ID: {self.idState.id} \nValue: {self.value} \n--------------------------------\n")
    
    def __lt__(self, other):
        
        return (self.value, self.idState.id[0], self.idState.id[1]) < (other.value, other.idState.id[0], other.idState.id[1])
        