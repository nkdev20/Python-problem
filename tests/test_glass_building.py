import unittest
import sys
sys.path.append("..")
from Libraries.GlassBuilding import GlassBuilding
from Libraries.Robot import Robot

class TestGlassBuilding(unittest.TestCase):
    
    def test_grid_creation(self):
        grid = [['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'E', 'E']]
        
        glass_building = GlassBuilding(3, 5)
        glass_building.construct_grid()

        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(grid[i][j] , glass_building.grid[i][j])
