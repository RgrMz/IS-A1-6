from classes.Node import Node
from classes.State import State 
from functionalities.problem_functions import successor_function                  
from classes.Cell import Cell
from functionalities.import_json import import_json
from maze_constants import MOVEMENTS
import random

random.seed()

def generate_random_nodes(limit_depth):
    
    states = []
    nodes = []
    maze = generate_random_maze()
    state = root = None
    for row in maze.get_grid():
        for cell in row:
            state = State(cell)
            states.append(state)
    
    cost = 0
    root = Node(0, cost, states[0], None, None, 0, 20)
    root.value = cost
    nodes.append(root)
    new_id = root.id
    
    ## TODO
    while (limit_depth > 0):

        # Successor (action, new state, cost) 
        new_id = new_id+1
        v = random.randint(1, 10) # Random value to increase the value
        h = random.randint(0, 20) # Random value for the heuristic
        new_node = Node(new_id, root.cost + random.randint(1,3), random.choice(states), root, random.choice(MOVEMENTS), root.depth + 1, h)
        new_node.value = root.cost + v      #later test with cost to generate more ties
        nodes.append(new_node)
            
        root = nodes[random.randint(0, len(nodes) - 1)]

        limit_depth = limit_depth - 1
    
    return nodes

def generate_random_maze():
    # Auxiliary function to obtain a maze to generate the nodes from
    return import_json("./json-mazes/Lab_10_25.json", False)
