from window import *
from tkinter import Tk, BOTH, Canvas



class Cell:
    
    def __init__(self, window=None):
        
        #wall check yuh
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        #coords
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        
        self.__win = window
        
        self.visited = False
        
        
    def draw(self, x1, y1, x2, y2):
        
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.__win == None:
            return

        point1 = Point(x1,y1)
        point2 = Point(x1,y2)
        line = Line(point1,point2)
        if self.has_left_wall:
            line.draw_line(self.__win.canvas_widget,"black")
        else:
            line.draw_line(self.__win.canvas_widget,"white")
        point1 = Point(x2,y1)
        point2 = Point(x2,y2)
        line = Line(point1,point2)
        if self.has_right_wall:
            line.draw_line(self.__win.canvas_widget,"black")
        else:
            line.draw_line(self.__win.canvas_widget,"white")

        point1 = Point(x1,y1)
        point2 = Point(x2,y1)
        line = Line(point1,point2)
        if self.has_top_wall:
            line.draw_line(self.__win.canvas_widget,"black")
        else:
            line.draw_line(self.__win.canvas_widget,"white")

        point1 = Point(x1,y2)
        point2 = Point(x2,y2)
        line = Line(point1,point2)
        if self.has_bottom_wall:
            line.draw_line(self.__win.canvas_widget,"black")
        else:
            line.draw_line(self.__win.canvas_widget,"white")
            
    def draw_move(self, to_cell, undo=False):
        
        colour = "red"
        if undo:
            colour = "gray"
            
        half_length = abs(self.__x2 - self.__x1) // 2
        x_center = half_length + self.__x1
        y_center = half_length + self.__y1

        half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
        x_center2 = half_length2 + to_cell.__x1
        y_center2 = half_length2 + to_cell.__y1
        
        if self.__win == None:
            return
        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self.__win.draw_line(line,colour)
                