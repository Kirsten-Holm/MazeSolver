from window import *

def main ():
    
    win = Window(800,600)
    win.draw_line(Line(Point(50,50),Point(500,500)),"BLACK")
    win.wait_for_close()
    
    
    
    

main()