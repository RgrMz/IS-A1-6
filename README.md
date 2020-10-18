# IS-A1-6

## MAZE GENERATOR
**Generate rectangular mazes**  
![alt text here](https://www.linkpicture.com/q/image_mazes2.png)  

With this program we have made these functionalities:
  + Given the number of rows and columns of an hypothetic maze it exports it as a json file with all its data and a jpeg image with the drawn maze.
  + Given a json file it check if the cells neighbours are consistent and it as well exports the jpeg image representing the maze.

Before running the program it is necessary to install two modules:
  + pygame: `python -m pip install -U pygame --user`
  + colorama: `python setup.py install --user` or if you have pip `pip install colorama --user`
  
  Note: If you dont have superuser privileges you can use `--user`. Otherwise just type `sudo <command>`

The way of running it is:
    + `python -B main.py`
  
