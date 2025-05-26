
from tkinter import Tk, BOTH, Canvas



class Window:
    
    def __init__(self, width, height):
        
        self.root_widget = Tk()
        
        self.root_widget.title("Maze Solver")
        
        self.canvas_widget = Canvas(self.root_widget, bg="white", height=height,width=width)

        self.canvas_widget.pack(fill=BOTH,expand=1)
        
        self.running = False
        
        self.root_widget.protocol("WM_DELETE_WINDOW",self.close)

    def redraw (self):
        
        self.root_widget.update()
        
        self.root_widget.update_idletasks()
        
        
    def wait_for_close (self):
        
        self.running = True
        
        while self.running:
            self.redraw()
            
        print("window closed...")
            
    def close (self):
        
        self.running = False
        
    def draw_line(self, Line, fill_color="BLACK"):
        
        Line.draw(self.canvas_widget,"BLACK")
        
        
        
        
class Point:
    
    def __init__(self, x, y):
        
        self.x = x
        
        self.y = y
        
        
        
class Line:
    
    def __init__(self, Point1, Point2):
        
        self.point1 = Point1
        
        self.point2 = Point2


    def draw(self, canvas, fill_color):
        
        canvas.create_line(self.point1.x,self.point1.y,self.point2.x,self.point2.y, fill=fill_color, width=2)
        




        
        
        

