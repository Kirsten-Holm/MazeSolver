import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
        
    def test_maze_break_entrance_and_exit(self):
        m1 = Maze(0,0,10,10,15,15)
        m1._Maze__break_entrance_and_exit()
        self.assertFalse(m1._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m1._Maze__cells[10-1][10-1].has_bottom_wall)
    
    def test_maze_reset_cells_visited(self):
        
        m1 = Maze(0,0,10,10,15,15)
        
        for col in m1._Maze__cells:
            for cell in col:
                self.assertFalse(cell.visited)
    
    
    
    
    
    
if __name__ == "__main__":
    unittest.main()