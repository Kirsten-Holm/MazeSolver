from tkinter import Tk, BOTH, Canvas
import time
from window import *
from cell import *
import random



class Maze:
    
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        #parameter values
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed != None:
            self.seed = random.seed(seed)
        #non parameter values
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        
    def __create_cells(self):
        
        for i in range(0,self.num_cols):
            self.__cells.append([])
            for j in range(0,self.num_rows):
                self.__cells[i].append(Cell(self.win))

        for i in range(0,len(self.__cells)):
            for j in range(0,len(self.__cells[i])):
                self.__draw_cell(i,j)
        
        
    def __draw_cell(self, i, j):
        x_cord = self.x1
        if i != 0:
            x_cord = self.cell_size_x * i + self.x1
        y_cord = self.y1
        if j != 0:
            y_cord = self.cell_size_y * j + self.y1
            
        if self.win == None:
            self.__cells[i][j].__x1 = x_cord
            self.__cells[i][j].__y1 = y_cord
            self.__cells[i][j].__x2 = x_cord + self.cell_size_x
            self.__cells[i][j].__y2 = x_cord + self.cell_size_y
        else:
            self.__cells[i][j].draw(x_cord,y_cord,x_cord+self.cell_size_x,y_cord+self.cell_size_y)
            self.animate()
        
    def animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(0.05)
        
        
        
    def __break_entrance_and_exit(self):
        
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.num_cols-1,self.num_rows-1)
        
            
    def __break_walls_r(self, i, j):
        
        self.__cells[i][j].visited = True
        
        while True:
            coords_to_visit = []
            if i + 1 < self.num_cols:
                if self.__cells[i+1][j].visited == False:
                    coords_to_visit.append((i + 1, j))
            if j + 1 < self.num_rows:
                if self.__cells[i][j+1].visited == False:
                    coords_to_visit.append((i, j + 1))
            if i - 1 >= 0:
                if self.__cells[i-1][j].visited == False:
                    coords_to_visit.append((i - 1, j))
            if j - 1 >= 0:
                if self.__cells[i][j-1].visited == False:
                    coords_to_visit.append((i, j - 1))
                    
            if len(coords_to_visit) == 0:
                return
            
            next_cell = coords_to_visit[random.randrange(0,len(coords_to_visit))]
            next_i = next_cell[0]
            next_j = next_cell[1]
            if next_i == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__draw_cell(i,j)
                self.__cells[next_i][next_j].has_left_wall = False
                self.__draw_cell(next_i,next_j)
            if next_i == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__draw_cell(i,j)
                self.__cells[next_i][next_j].has_right_wall = False
                self.__draw_cell(next_i,next_j)
            if next_j == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__draw_cell(i,j)
                self.__cells[next_i][next_j].has_top_wall = False
                self.__draw_cell(next_i,next_j)
            if next_j == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__draw_cell(i,j)
                self.__cells[next_i][next_j].has_bottom_wall = False
                self.__draw_cell(next_i,next_j)
                
            self.__break_walls_r(next_i,next_j)

                

            
        
        