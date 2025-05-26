
from tkinter import Tk, BOTH, Canvas



class Window:
    
    def __init__(self, width, height):
        
        self.root_widget = Tk()
        
        self.root_widget.title = f"{width}/{height}"
        
        self.canvas_widget = Canvas()

        self.canvas_widget.pack()
        
        self.running = False
        
    def redraw (self):
        
        self.root_widget.update()
        
        self.root_widget.update_idletasks()
        
        
    def wait_for_close (self):
        
        self.running = True
        
        while self.running:
            self.redraw()
            
    def close (self):
        
        self.running = False
        
        self.root_widget.protocol("WM_DELETE_WINDOW",self.close)
        
        
        

