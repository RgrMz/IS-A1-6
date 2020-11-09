from time import time   # To measure the execution time
from classes.Node import Node
from classes.Frontier import Frontier
from classes.FrontierDeque import FrontierDeque
from classes.FrontierList import FrontierList

####        STATISTICAL COMPARISON      ####

def execution_time(nodes, frontier):
    
    initial_time = time()
    
    for node in nodes:
        frontier.push(node)
    pushed_time = time()
    
    while not(frontier.isEmpty()):
        aux = frontier.pop()
    popped_time = time()
    
    final_time = time()

    # Total execution, time to push all, time to pop all
    return final_time - initial_time, pushed_time - initial_time, popped_time - pushed_time

