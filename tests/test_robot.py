import unittest
from robot_exceptions import DirectionError, RobotPlacementError
from robot import Robot


class TestRobotInitialisation(unittest.TestCase):

    def setUp(self):
        pass

    def test_with_correct_args_initialises_robot(self):
        test_robot = Robot(0, 0, "North")
        self.assertIsInstance(test_robot, Robot)

    def test_with_invalid_type_y_coordinate_raises_typeerror(self):
        self.assertRaises(TypeError, Robot, 3, "", "North")

    def test_with_invalid_type_x_coordinate_raises_typeerror(self):
        self.assertRaises(TypeError, Robot, {}, 4, "East")

    def test_with_invalid_direction_raises_direction_error(self):
        self.assertRaises(DirectionError, Robot, 3, 4, "dunno")

    def test_with_x_coordinate_larger_than_table_size_raises_robot_placement_error(self):
        self.assertRaises(RobotPlacementError, Robot, 5, 5, "West")
