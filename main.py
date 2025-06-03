from window import *
from cell import *
from maze import *

def main ():
    
    win = Window(800,600)
    maze = Maze(10,10,5,5,25,30,win)

    maze._Maze__break_entrance_and_exit()
    
    maze._Maze__cells[2][2].draw_move(maze._Maze__cells[4][4])
    
    win.wait_for_close()
    
    
    
    

main()