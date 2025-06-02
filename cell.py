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
        
        
    def draw(self, x1, y1, x2, y2):
        
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.__win == None:
            return
        if self.has_left_wall:
            point1 = Point(x1,y1)
            point2 = Point(x1,y2)
            line = Line(point1,point2)
            line.draw_line(self.__win.canvas_widget,"black")
        if self.has_right_wall:
            point1 = Point(x2,y1)
            point2 = Point(x2,y2)
            line = Line(point1,point2)
            line.draw_line(self.__win.canvas_widget,"black")
        if self.has_top_wall:
            point1 = Point(x1,y1)
            point2 = Point(x2,y1)
            line = Line(point1,point2)
            line.draw_line(self.__win.canvas_widget,"black")
        if self.has_bottom_wall:
            point1 = Point(x1,y2)
            point2 = Point(x2,y2)
            line = Line(point1,point2)
            line.draw_line(self.__win.canvas_widget,"black")
            
    def draw_move(self, to_cell, undo=False):
        
        colour = "red"
        if undo:
            colour = "gray"
            
        cell_size = 50
        cell_size /= 2
        line_to_draw = Line(Point(self.__x1+cell_size,self.__y1+cell_size),
                            Point(to_cell.__x1+cell_size,to_cell.__y1+cell_size))
        if self.__win == None:
            return
        self.__win.draw_line(line_to_draw,colour)
                