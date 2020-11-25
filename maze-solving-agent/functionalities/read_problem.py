from functionalities.import_json import import_json
from classes.State import State
from classes.Cell import Cell
from classes.Problem import Problem
import json

def read_problem(file_name):
    
    """
        Description:
            This function gets the name of a file to read it to get the information needed to initialize
            and then solve the problem
        Parameters:
            file_name (String): the name of the JSON file containing the problem information.
    """
    with open(file_name) as file:
        problemDict = json.load(file)
    
    initialPosition = eval(problemDict["INITIAL"])
    finalPosition = eval(problemDict["OBJETIVE"])
    maze = import_json(problemDict["MAZE"], False)
    initialState = State(maze.get_cell(initialPosition[0], initialPosition[1]))
    finalState = State(maze.get_cell(finalPosition[0], finalPosition[1]))
    
    return Problem(maze, initialState, finalState)   
