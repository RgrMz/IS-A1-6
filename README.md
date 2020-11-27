# IS-A1-6

## MAZE SOLVING AGENT
**Generate rectangular mazes**  
![alt text here](https://www.linkpicture.com/q/image_mazes2.png)  

### What does this software do?
This software has been designed for our Intelligent Systems course laboratory sessions, in which we have designed and implemented an agent that, given a maze, and also a starting (it can be seen as the **entry** of the maze) cell and the final (it can be seen as the **exit** of the maze) cell, it is able to enter the maze and exit from it. It does not matter how **large** the maze is: it will exit from it if there exists a **path** connectin the entry of the maze with the exit.

Above, the problem this software solves, has been expressed without any **theoretical** terminology, but for our course, the concepts that are practiced by implementing this software are:
  - Implementation of a **search algorithm** in a **state space** represented by the cells of the maze.
 
### Which functionalities does this software have? 
This software is used via **command line**, in which a **menu** with the functionalities that this software offers are presented. Through the development of this software, we have implemented the following features
  1. Generate a random maze given the **number of rows and columns** of an hypothetic maze it exports it as a **JSON file** with all its data and a **PNG image with the drawn maze**.
  2. Given a **JSON file** it checks if the maze is **consistent** and it as well exports the **PNG image representing the maze**.
  3. Define a **problem** by providing a JSON file with the **maze** to be used in the problem.
  4. Compare different data structures that were considered for the selection of a data structure used in the search algorithm called *frontier*. If you want to see these time comparions, just slect this option.
  5. Give the **file name** of a JSON file containing a **problem** and a **strategy** to solve it among these five: `BREADTH ; DEPTH ; UNIFORM ; GREEDY ; A` and the software will solve the problem using this strategy providing:
      - A PNG image of the maze selected.
      - A PNG image coloured with the **solution path** in red.
      - A .txt file containing the **solution path** as a list of items called **nodes**. 
  6. Exit the program.

Before running the program it is necessary to install two modules:
  + pygame: `python -m pip install -U pygame --user`
  + colorama: `python setup.py install --user` or if you have pip `pip install colorama --user`
  
  Note: If you dont have superuser privileges you can use `--user`. Otherwise just type `sudo <command>`

The way of running it is:

    1. Move yourself into the folder `Subtask1` with `cd Subtask1/`
    
    2. Execute the command `python -B main.py` if you have installed Python3 or a superior version, otherwise `python3 -B main.py`
    
    3. Interact with the command line menu to obtain the desired result
  
