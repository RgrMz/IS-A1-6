import sys
import random
from classes.Maze import Maze
from classes.ConsistencyError import ConsistencyError
from classes.Frontier import Frontier
from classes.FrontierDeque import FrontierDeque
from classes.FrontierList import FrontierList
from functionalities.import_json import import_json
from functionalities.export import export_json, export_image, define_problem
from functionalities.wilsons_algorithm import generate_maze
from functionalities.generate_random_nodes import generate_random_nodes
from functionalities.frontier_testing import execution_time

# Colored text
from colorama import Fore
    
def menu():
    
    """
        Description:
            This function works as a menu of the program, it includes all the options
            it offers.
    """
    
    correct = False
    num_opt = -1
    print(f"""{Fore.BLUE}

 _       __   ____  ____      __    ____  _      ____  ___    __   _____  ___   ___  
| |\/|  / /\   / / | |_      / /`_ | |_  | |\ | | |_  | |_)  / /\   | |  / / \ | |_) 
|_|  | /_/--\ /_/_ |_|__     \_\_/ |_|__ |_| \| |_|__ |_| \ /_/--\  |_|  \_\_/ |_| \ 

{Fore.RESET}""")
    while num_opt != 4:

        while not correct:
            num_opt = int(input(f"""\nSelect the functionality you want to use:\n
[1] Create a maze and export a JSON file and a JPEG image.\n
[2] Import a JSON file to produce the maze and export the JPEG image of it.\n
[3] Export problem to a JSON.\n
[4] Compare the different frontier structures.\n{Fore.LIGHTCYAN_EX}
[5] Exit.{Fore.RESET}\n"""))
            if num_opt < 1 or num_opt > 4:
                print(f"{Fore.RED}Invalid option.{Fore.RESET}\n")
            else:
                correct = True
        # Create a maze and export the JSON and the image
        if num_opt == 1:
            try:
                number_rows = int(input("Introduce the number of ROWS.\n"))
                number_columns = int(input("Introduce the number of COLUMNS.\n"))
            except Exception as error: 
                print(f"{Fore.RED}")
                print("Error ocurred: {}".format(error))
                print(f"{Fore.RESET}")
                continue
                
            if (number_rows > 0):
                if (number_columns > 0):

                    maze = Maze(number_rows, number_columns)
                    generate_maze(maze)
                    export_json(maze)
                    export_image(maze)
                    print(f"{Fore.GREEN}The maze was succesfully created!{Fore.RESET}")
                    correct = False
                    continue
                else:
                    print(f"{Fore.RED}You have to introduce a valid number of COLUMNS.{Fore.RESET}")
            else:
                print(f"{Fore.RED}You have to introduce a valid number of ROWS.{Fore.RESET}")
        # Import the JSON file to then export the image
        elif num_opt == 2:
            
            try:
                import_json(input("Please introduce the file name.\n"))
                print(f"{Fore.GREEN}The maze was succesfully imported and exported as an image!{Fore.RESET}")
            except Exception as error:
                print(f"{Fore.RED}")
                print("Error ocurred: {}".format(error))
                print(f"{Fore.RESET}")
            correct = False
            continue
        
        elif num_opt == 3:
            try:
                define_problem(input("Please introduce the file name.\n"))
                print(f"{Fore.GREEN}The problem was succesfully defined and exported!{Fore.RESET}")
            except Exception as error:
                print(f"{Fore.RED}") 
                print("Error ocurred: {}".format(error))
                print(f"{Fore.RESET}")
            correct = False
            continue

        elif num_opt == 4:
            
            frontier = Frontier()
            frontierDeque = FrontierDeque()
            frontierList = FrontierList()
            
            # Checking the correct insertion in the frontier
            nodes = generate_random_nodes(20)
            for node in nodes:
                frontier.push(node)
            while not(frontier.isEmpty()):
                print(frontier.pop().toString())
                
            # Comparing the candidate structures for frontier
            for value in [500, 1000, 10000, 20000, 1000000]:
                nodes = generate_random_nodes(value)

                total_time, pushed_time, popped_time = execution_time(nodes, frontier)
                print(f"Frontier Heapq {value}: \n  - Total execution time: {total_time} \n  - Total push time: {pushed_time} \n  - Total pop time: {popped_time} ")
                if value != 1000000:
                    total_time, pushed_time, popped_time = execution_time(nodes, frontierDeque)
                    print(f"Frontier Deque {value}: \n  - Total execution time: {total_time} \n  - Total push time: {pushed_time} \n  - Total pop time: {popped_time} ")
                    total_time, pushed_time, popped_time = execution_time(nodes, frontierList)
                    print(f"Frontier List {value}: \n  - Total execution time: {total_time} \n  - Total push time: {pushed_time} \n  - Total pop time: {popped_time} ")
            
        elif num_opt == 5:
            print(f"{Fore.LIGHTCYAN_EX}Thanks for using our program! Come back soon.{Fore.RESET}")
            exit()
                    
def main():
    
    """
        Description:
            This is the main function of the program, it calls the menu function so that it shows
            the user the functionalities it offers
    """
    menu()
 
if __name__ == "__main__": 
    main()