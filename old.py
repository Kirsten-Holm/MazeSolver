


#file for old code that i felt like keeping for reference

cells = []
coords = []
cell_size = 50
x_length = 10
y_length = 10
for y in range(1,y_length+1):
    for x in range (1,x_length):
        coords.append((cell_size*x,y*cell_size,cell_size*x+cell_size,cell_size*y+cell_size))
    
for set in coords:
    cells.append(Cell(win))
    
    
for cell in range(0,len(cells)):
    current_cell = cells[cell]
    
    current_cell.draw(coords[cell][0],coords[cell][1],coords[cell][2],coords[cell][3])
    
cells[0].draw_move(cells[28])
