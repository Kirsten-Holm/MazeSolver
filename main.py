from window import *
from cell import *
from maze import *

def main ():
    
    win = Window(800,600)
    maze = Maze(10,10,25,25,30,30,win)


    maze.solve()

    
    win.wait_for_close()
    
    
    
    

main()