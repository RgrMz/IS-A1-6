from time import time   # To measure the execution time
import sys
from classes.Cell import Cell
from classes.State import State
from classes.Node import Node
from classes.Frontier import Frontier
from classes.FrontierDeque import FrontierDeque
from classes.FrontierList import FrontierList

# import resource       # Uncomment this import if you want to run maximum_number_nodes

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

    # Total execution time, time to push all, time to pop all
    return final_time - initial_time, pushed_time - initial_time, popped_time - pushed_time

####    WARNING: the below function to check the maximum number of nodes
####    that can be stored in frontier only runs under UNIX environment, not in Windows
####    Uncomment if you want to test it 

# def maximum_number_nodes(frontier):
    
#     count = 0
#     state = State(Cell(3,4))

#     #   Creating empty nodes
#     while resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/10**6 < 2:
#         try:        
#             node = Node(0, 0, state, None, None, 0, 0)
#             node.value = 0
#             frontier.push(node)
#             count = count + 1
            
#         except MemoryError:
#             sys.stderr.write("Memory consumed: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/10**6) + " GB" + "\nNumber of elements stored: " + str(count) + " elements\n")
#             sys.exit(-1)
#     sys.stderr.write("\n\nMemory consumed: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/10**6) + " GB" + "\n\nNumber of elements stored: " + str(count) + " elements\n\n\n")

