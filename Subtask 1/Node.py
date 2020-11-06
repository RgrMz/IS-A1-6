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