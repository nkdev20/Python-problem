import unittest
import sys
sys.path.append("..")
from Libraries.GlassBuilding import GlassBuilding
from Libraries.Robot import Robot

class TestRobot(unittest.TestCase):
    
    def test_move_left(self):
        robo = Robot('robo', [0, 0 , 'N' , 'R'])
        robo.move_left()
        self.assertEqual('W', robo.direction)

    def test_move_right(self):
        robo = Robot('robo', [0, 0 , 'N' , 'R'])
        robo.move_right()
        self.assertEqual('E', robo.direction)

    
    def test_move_forward_by_one_cell(self):
        robo = Robot('robo', [0, 0 , 'N' , 'R'])
        robo.forward_by_one_cell()
        self.assertEqual(1, robo.y_cordinate)

    def test_fill(self):
        glass_building = GlassBuilding(5, 5)
        glass_building.construct_grid()
        robo = Robot('robo', [0, 0 , 'N' , 'R'])
        robo.fill(glass_building)
        self.assertEqual('R', glass_building.grid[4][0])