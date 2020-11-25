from classes.Node import Node
from classes.Frontier import Frontier
from classes.MaximumDepthReachedException import MaximumDepthReachedException
from functionalities.problem_functions import heuristic_function, goal_function, successor_function
from maze_constants import MAXIMUM_DEPTH

def search(problem, frontier, strategy):
    
    """
        Description:
            Algorithm used to find a solution to a problem introduced by the user. It takes it and 
            applies a concrete strategy to do so. If it finds a solution it returns the last node, if 
            there is no solution it returns Failuredatetime A combination of a date and a time. 
            
        Parameters:
            problem (Problem): Representation of the problem
            frontier (Frontier): Heapq that contains the nodes in the frontier of the search
            strategy (String): Strategy chosen by the user to use in the search
    """
    
    visited = set()
    heuristic = heuristic_function(problem.initialState.id[0], problem.initialState.id[1], problem.finalState.id[0], problem.finalState.id[1])
    root = Node(0, 0, problem.initialState, None, None, 0, heuristic)
    if strategy == "DEPTH": root.value = 1.0
    elif strategy == "GREEDY" or strategy == "A": root.value = heuristic
    
    frontier.push(root)
    
    while not(frontier.isEmpty()):
        
        node = frontier.pop()
        
        if goal_function(node.idState.id, problem.finalState.id):
            return node, frontier, visited      # Ask to the professor if we can do this
                                                # Maybe we need to condensar the code to avoid muchas llamadas en el main
        
        if not(node.idState.id in visited):
            visited.add(node.idState.id)
            for newNode in expand(node, problem, strategy):
                frontier.push(newNode)
        
    return None # Failure
                

def expand(node, problem, strategy):
    
    """
        Description:
            Function which takes a Node object and returns the list of successors Nodes which can be accessed from it
            in the search tree
        Parameters:
            node (Node): the node to be expanded
            problem (Problem): Representation of the problem
            frontier (Frontier): Heapq that contains the nodes in the frontier of the search
            strategy (String): Strategy chosen by the user to use in the search
    """
    
    successorsNodes = list()
    
    for successor in successor_function(problem, node.idState):
        newDepth = node.depth+1
        if newDepth > MAXIMUM_DEPTH:
            raise MaximumDepthReachedException("Maximum depth for searching has been reached: {0}".format(MAXIMUM_DEPTH))
        
        problem.lastId += 1
        newState = problem.stateSpace[successor[1]]
        heuristic = heuristic_function(successor[1][0], successor[1][1], problem.finalState.id[0], problem.finalState.id[1])
        
        newNode = Node(problem.lastId, node.cost + successor[2], newState, node, successor[0], newDepth, heuristic)
            
        if strategy.upper() == 'BREADTH':
            newNode.value = newNode.depth
        
        elif strategy.upper() == "DEPTH":
            newNode.value = float(1/(newNode.depth+1))
        
        elif strategy.upper() == "UNIFORM":
            newNode.value = newNode.cost
            
        elif strategy.upper() == "GREEDY":
            newNode.value = newNode.heuristic
            
        elif strategy.upper() == "A":
            newNode.value = newNode.heuristic + newNode.cost
            
        successorsNodes.append(newNode)
        
    return successorsNodes

def find_solution(node):
    
    """
        Description:
            Function which take the node object objective and find its parent iteratively so finally 
            it reaches the root creating the solution. 
        Parameters:
            node (Node): the node objective of the problem.

    """
    
    nodeStack = [] 
    nodeStack.append(node) 
    while node.idParent != None: 
        nodeStack.append(node.idParent)
        # Update the current node to get to the parent
        node = node.idParent  
    return nodeStack
    