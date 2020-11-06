from .. import Node, State 
import successor_function as sfn                  
import random
from ..classes.Cell import Cell
import import_json
import random

random.seed()

def generate_random_nodes(limit_depth):
    
    limit_depth = 6
    states = []
    nodes = []
    maze = generate_random_maze()
    for row in maze.get_grid():
        for cell in row:
            states.append(State(cell))
    
    cost = 0
    root = Node(0, cost, states[0], None, None, 0, 20) 
    root.value = cost
    nodes.append(root)
    
    new_id = root.id

    while limit_depth > 0:
        # Create new nodes, for each iteration we can create 2 or 3 
        # which have a parent previously created
        successors = sfn(root.idState)
        for successor in successors:
            # Successor (accion, state nuevo, coste) 
            new_id = new_id+1
            v = random.randrange(0, 5, [1]) # Random value to increase the value
            h = random.randrange(0, 5, [1]) # Random value for the heuristic
            new_node = Node((new_id), root.cost + successor[2], successor[1], root, successor[0], root.depth + 1, h)
            new_node.value = root.cost + v      #later test with cost to generate more ties
            nodes.append(new_node)
        
        root = nodes[len(nodes) - 1]
          
        # linked list
        # binary tree
        # heap

        limit_depth = limit_depth - 1
    
    return nodes
        
        

def generate_random_maze():
    
    return import_json("../json-mazes/Lab_10_10.json", False)