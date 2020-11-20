from classes.Node import Node
from classes.Frontier import Frontier
from functionalities.problem_functions import heuristic_function, goal_function, successor_function

def search(problem, frontier, strategy):
    
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
    
    successorsNodes = list()
    # newID = node.id + 1
    
    for successor in successor_function(problem, node.idState):
        
        problem.lastId += 1
        newState = problem.stateSpace[successor[1]]
        heuristic = heuristic_function(successor[1][0], successor[1][1], problem.finalState.id[0], problem.finalState.id[1])
        
        newNode = Node(problem.lastId, node.cost + successor[2], newState, node, successor[0], node.depth + 1, heuristic)
        
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
    
    nodeStack = [] 
    nodeStack.append(node) 
    while node.idParent != None: 
        nodeStack.append(node.idParent)
        # Update the current node to get to the parent
        node = node.idParent  
    return nodeStack
    