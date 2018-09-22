import unittest
from table import Table


class TestTableInitialisation(unittest.TestCase):
    def setUp(self):
        pass

    def test_with_correct_args(self):
        test_table = Table(2, 2)
        self.assertIsInstance(test_table, Table)

    def test_with_invalid_type_args_raises_typeerror(self):
        self.assertRaises(TypeError, Table, "", "")

    def test_with_invalid_type_length_raises_typeerror(self):
        self.assertRaises(TypeError, Table, "", 3)

    def test_with_invalid_type_breadth_raises_typeerror(self):
        self.assertRaises(TypeError, Table, 3, "")


class TestPositionValidator(unittest.TestCase):
    def setUp(self):
        self.test_table = Table(2, 2)

    def test_with_a_bigger_position_than_the_board_return_false(self):
        self.assertFalse(self.test_table.position_validator(5))

    def test_with_a_equal_position_than_the_board_return_true(self):
        self.assertTrue(self.test_table.position_validator(1))

    def test_with_a_smaller_position_than_the_board_returns_true(self):
        self.assertTrue(self.test_table.position_validator(0))
