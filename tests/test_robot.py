import unittest
from robot_exceptions import DirectionError, RobotPlacementError
from robot import Robot


class TestRobotInitialisation(unittest.TestCase):

    def setUp(self):
        self.test_robot = Robot(0, 0, "North")

    def test_with_correct_args_initialises_robot(self):
        self.assertIsInstance(self.test_robot, Robot)

    def test_with_invalid_type_y_coordinate_raises_typeerror(self):
        self.assertRaises(TypeError, Robot, 3, "", "North")

    def test_with_invalid_type_x_coordinate_raises_typeerror(self):
        self.assertRaises(TypeError, Robot, {}, 4, "East")

    def test_with_invalid_direction_raises_direction_error(self):
        self.assertRaises(DirectionError, Robot, 3, 4, "dunno")

    def test_with_x_coordinate_larger_than_table_size_raises_robot_placement_error(self):
        self.assertRaises(RobotPlacementError, Robot, 5, 5, "West")

    def test_with_larger_x_or_y_coordinate_raises_robot_placement_error(self):
        self.assertRaises(RobotPlacementError, self.test_robot.place, 5, 90, "North")

    def test_with_valid_x_and_y_coordinate_but_invalid_direction_raises_direction_error(self):
        self.assertRaises(DirectionError, self.test_robot.place, 3, 3, "where are you?")


class TestReport(unittest.TestCase):

    def setUp(self):
        self.test_robot = Robot(0, 0, "North")

    def test_with_valid_args_places_robot_on_table(self):
        expected_output = "Output: 0,0,North"
        self.assertEqual(expected_output, self.test_robot.report())


class TestMove(unittest.TestCase):

    def setUp(self):
        self.test_robot = Robot(0, 0, "North")

    def test_with_valid_args_moves_robot_one_step_forward_y_axis_on_table(self):
        self.test_robot.place(2, 3, "North")
        self.test_robot.move()
        expected_output = "Output: 2,4,North"
        self.assertEqual(expected_output, self.test_robot.report())

    def test_with_valid_args_greater_than_table_size_raises_robot_placement_error(self):
        self.test_robot.place(2, 4, "North")
        self.assertRaises(RobotPlacementError, self.test_robot.move)

    def test_with_valid_args_moves_robot_one_step_back_y_axis_on_table(self):
        self.test_robot.place(2, 4, "South")
        self.test_robot.move()
        expected_output = "Output: 2,3,South"
        self.assertEqual(expected_output, self.test_robot.report())

    def test_with_valid_args_moves_robot_one_step_to_x_axis_on_table(self):
        self.test_robot.place(2, 4, "East")
        self.test_robot.move()
        expected_output = "Output: 3,4,East"
        self.assertEqual(expected_output, self.test_robot.report())

    def test_with_valid_args_moves_robot_one_step_back_to_x_axis_on_table(self):
        self.test_robot.place(2, 4, "West")
        self.test_robot.move()
        expected_output = "Output: 1,4,West"
        self.assertEqual(expected_output, self.test_robot.report())

    def test_with_valid_args_with_west_end_of_table_raises_robot_placement_error(self):
        self.test_robot.place(0, 4, "West")
        self.assertRaises(RobotPlacementError, self.test_robot.move)

    def test_with_valid_args_with_east_end_of_table_raises_robot_placement_error(self):
        self.test_robot.place(4, 4, "East")
        self.assertRaises(RobotPlacementError, self.test_robot.move)


class TestLeft(unittest.TestCase):

    def setUp(self):
        self.test_robot = Robot(0, 0, "North")

    def test_with_valid_args_turns_robot_left_from_north_on_table(self):
        self.test_robot.place(2, 3, "North")
        self.test_robot.left()
        expected_output = "Output: 2,3,West"
        self.assertEqual(expected_output, self.test_robot.report())

    def test_with_valid_args_turns_robot_left_from_east_on_table(self):
        self.test_robot.place(2, 3, "East")
        self.test_robot.left()
        expected_output = "Output: 2,3,North"
        self.assertEqual(expected_output, self.test_robot.report())


class TestRight(unittest.TestCase):

    def setUp(self):
        self.test_robot = Robot(0, 0, "North")

    def test_with_valid_args_turns_robot_right_from_south_on_table(self):
        self.test_robot.place(2, 3, "South")
        self.test_robot.right()
        expected_output = "Output: 2,3,West"
        self.assertEqual(expected_output, self.test_robot.report())

    def test_with_valid_args_turns_robot_left_from_east_on_table(self):
        self.test_robot.place(2, 3, "East")
        self.test_robot.right()
        expected_output = "Output: 2,3,South"
        self.assertEqual(expected_output, self.test_robot.report())
