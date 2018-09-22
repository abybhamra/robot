import unittest
from remote import Remote
from robot_exceptions import RobotPlacementError, DirectionError


class TestPlace(unittest.TestCase):

    def setup(self):
        pass

    def test_with_valid_args_places_robot_on_table(self):
        test_remote = Remote()
        test_remote.place(0, 0, "North")
        expected_output = "Output: 0,0,North"
        self.assertEqual(expected_output, test_remote.report())

    def test_with_larger_x_or_y_coordinate_raises_robot_placement_error(self):
        test_remote = Remote()
        self.assertRaises(RobotPlacementError, test_remote.place, 5, 90, "North")

    def test_with_valid_x_and_y_coordinate_but_invalid_direction_raises_direction_error(self):
        test_remote = Remote()
        self.assertRaises(DirectionError, test_remote.place, 3, 3, "where are you?")


class TestReport(unittest.TestCase):

    def setup(self):
        pass

    def test_with_valid_args_places_robot_on_table(self):
        test_remote = Remote()
        test_remote.place(0, 0, "North")
        expected_output = "Output: 0,0,North"
        self.assertEqual(expected_output, test_remote.report())

    def test_with_larger_x_or_y_coordinate_raises_robot_placement_error(self):
        test_remote = Remote()
        self.assertRaises(RobotPlacementError, test_remote.place, 5, 90, "North")

    def test_with_valid_x_and_y_coordinate_but_invalid_direction_raises_direction_error(self):
        test_remote = Remote()
        self.assertRaises(DirectionError, test_remote.place, 3, 3, "where are you?")


class TestMove(unittest.TestCase):

    def setup(self):
        pass

    def test_with_valid_args_moves_robot_one_step_forward_y_axis_on_table(self):
        test_remote = Remote()
        test_remote.place(2, 3, "North")
        test_remote.move()
        expected_output = "Output: 2,4,North"
        self.assertEqual(expected_output, test_remote.report())

    def test_with_valid_args_greater_than_table_size_raises_robot_placement_error(self):
        test_remote = Remote()
        test_remote.place(2, 4, "North")
        self.assertRaises(RobotPlacementError, test_remote.move)

    def test_with_valid_args_moves_robot_one_step_back_y_axis_on_table(self):
        test_remote = Remote()
        test_remote.place(2, 4, "South")
        test_remote.move()
        expected_output = "Output: 2,3,South"
        self.assertEqual(expected_output, test_remote.report())

    def test_with_valid_args_moves_robot_one_step_to_x_axis_on_table(self):
        test_remote = Remote()
        test_remote.place(2, 4, "East")
        test_remote.move()
        expected_output = "Output: 3,4,East"
        self.assertEqual(expected_output, test_remote.report())

    def test_with_valid_args_moves_robot_one_step_back_to_x_axis_on_table(self):
        test_remote = Remote()
        test_remote.place(2, 4, "West")
        test_remote.move()
        expected_output = "Output: 1,4,West"
        self.assertEqual(expected_output, test_remote.report())

    def test_with_valid_args_with_west_end_of_table_raises_robot_placement_error(self):
        test_remote = Remote()
        test_remote.place(0, 4, "West")
        self.assertRaises(RobotPlacementError, test_remote.move)

    def test_with_valid_args_with_east_end_of_table_raises_robot_placement_error(self):
        test_remote = Remote()
        test_remote.place(4, 4, "East")
        self.assertRaises(RobotPlacementError, test_remote.move)


class TestLeft(unittest.TestCase):

    def setup(self):
        pass

    def test_with_valid_args_turns_robot_left_from_north_on_table(self):
        test_remote = Remote()
        test_remote.place(2, 3, "North")
        test_remote.left()
        expected_output = "Output: 2,3,West"
        self.assertEqual(expected_output, test_remote.report())

    def test_with_valid_args_turns_robot_left_from_east_on_table(self):
        test_remote = Remote()
        test_remote.place(2, 3, "East")
        test_remote.left()
        expected_output = "Output: 2,3,North"
        self.assertEqual(expected_output, test_remote.report())


class TestRight(unittest.TestCase):

    def setup(self):
        pass

    def test_with_valid_args_turns_robot_right_from_south_on_table(self):
        test_remote = Remote()
        test_remote.place(2, 3, "South")
        test_remote.right()
        expected_output = "Output: 2,3,West"
        self.assertEqual(expected_output, test_remote.report())

    def test_with_valid_args_turns_robot_left_from_east_on_table(self):
        test_remote = Remote()
        test_remote.place(2, 3, "East")
        test_remote.right()
        expected_output = "Output: 2,3,South"
        self.assertEqual(expected_output, test_remote.report())
