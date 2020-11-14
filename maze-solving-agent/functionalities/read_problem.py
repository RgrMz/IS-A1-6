from functionalities.import_json import import_json
from classes.State import State
import json

def read_problem(file_name):
    
    with open(file_name) as file:
        problem = json.load(file)
        
    #return maze, initial_state (ya vemos si como objeto state o tuple) y final_state (same)