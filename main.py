from window import *
from cell import *
from maze import *

def main ():
    
    win = Window(800,600)
    maze = Maze(10,10,20,15,25,30,win)

    
    
    win.wait_for_close()
    
    
    
    

main()