class Node():
    
    """
        Class Description:
            This class is used to represent a node, containing essential information such as
            the id, cost, its state, its parent, action performed, the depth, heuristic and value
    """
    
    def __init__(self, idNode, cost, newState, parent, action, depth, heuristic):
        
        self.id = idNode
        self.cost = cost
        self.idState = newState
        self.idParent = parent
        self.action = action
        self.depth = depth
        self.heuristic = heuristic
        self.value = 0
    """
        Description:
            Returns as a string the information required to show from a node.
    """
    def toString (self):
        
        nodeString = ''
        if self.id == 0:  
            nodeString = f'\n[{self.id}][{self.cost},{self.idState.id},{self.idParent},{self.action},{self.depth},{self.heuristic},{self.value}]'
        else:
            nodeString = f'\n[{self.id}][{self.cost},{self.idState.id},{self.idParent.id},{self.action},{self.depth},{self.heuristic},{self.value}]'
        return nodeString
    
    """
        Description:
            Compares a Node with another one to establish an order criterion among nodes when they are stored in the frontier.
        Parameters:
            other (Node): a Node object to be compared with the current one in order to decide the order priority.
    """
    def __lt__(self, other):
        # To solve ambiguity: [value][row][column][node_id] as the node id is unique we won't have 
        #problems stablishing the order
        return (self.value, self.idState.id[0], self.idState.id[1], self.id) < (other.value, other.idState.id[0], other.idState.id[1], other.id)
        