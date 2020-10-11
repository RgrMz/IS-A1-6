import sys
import random
from classes.Maze import Maze
from classes.ConsistencyError import ConsistencyError
from functionalities.import_json import *
from functionalities.export import *
from functionalities.wilsons_algorithm import *
# Colored text
from colorama import Fore

# Random seed to get the random cells
random.seed()
    
def menu():
    correct = False
    num_opt = -1
    print(f"""{Fore.BLUE}

 _       __   ____  ____      __    ____  _      ____  ___    __   _____  ___   ___  
| |\/|  / /\   / / | |_      / /`_ | |_  | |\ | | |_  | |_)  / /\   | |  / / \ | |_) 
|_|  | /_/--\ /_/_ |_|__     \_\_/ |_|__ |_| \| |_|__ |_| \ /_/--\  |_|  \_\_/ |_| \ 

{Fore.RESET}""")
    while num_opt != 3:

        while not correct:
            num_opt = int(input(f"""\nSelect the functionality you want to use:\n
[1] Create a maze and export a JSON file and a JPEG image.\n
[2] Import a JSON file to produce the maze and export the JPEG image of it.\n{Fore.LIGHTCYAN_EX}
[3] Exit.{Fore.RESET}\n"""))
            if num_opt < 1 or num_opt > 3:
                print(f"{Fore.RED}Invalid option.{Fore.RESET}\n")
            else:
                correct = True
    
        if num_opt == 1:
            number_rows = int(input("Introduce the number of ROWS.\n"))
            number_columns = int(input("Introduce the number of COLUMNS.\n"))

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
            
            print(f"{Fore.LIGHTCYAN_EX}Thanks for using our program! Come back soon .{Fore.RESET}")
            exit()
                    
def main():
    menu()
    
if __name__ == "__main__": 
    main()