"""Class to represent the robot
"""
from table import Table
from robot_exceptions import DirectionError, RobotPlacementError

DIRECTIONS = ["West", "South", "East", "North"]
SIDE = 5
TABLE = Table(SIDE, SIDE)


class Robot(object):

    def __init__(self, x, y, direction):
        self.place(x, y, direction)

    @property
    def current_x_coordinate(self):
        """Read only property representing the x coordinate of the robot
        """
        return self.__current_x_coordinate

    @current_x_coordinate.setter
    def current_x_coordinate(self, x_coordinate):
        """Setter function to set the x coordinate of the robot

        :arg x_coordinate(int) : x coordinate of the robot
        """
        if not isinstance(x_coordinate, int):
            raise TypeError("x coordinate must be set to an integer")
        if x_coordinate >= SIDE or x_coordinate < 0:
            raise RobotPlacementError("x coordinate cant be greater than table side, robot will die!")
        self.__current_x_coordinate = x_coordinate

    @property
    def current_y_coordinate(self):
        """Read only property representing the y coordinate of the robot
        """
        return self.__current_y_coordinate

    @current_y_coordinate.setter
    def current_y_coordinate(self, y_coordinate):
        """Setter function to set the y coordinate of the robot

        :arg y_coordinate(int) : y coordinate of the robot
        """
        if not isinstance(y_coordinate, int):
            raise TypeError("y coordinate must be set to an integer")
        if y_coordinate >= SIDE or y_coordinate < 0:
            raise RobotPlacementError("x coordinate cant be greater than table side, robot will die!")
        self.__current_y_coordinate = y_coordinate

    @property
    def current_direction(self):
        """Read only property representing the current direction of the robot
        """
        return self.__current_direction

    @current_direction.setter
    def current_direction(self, direction):
        """Setter function to set the direction of the robot

        :arg direction(str) : direction of the robot
        :raise DirectionError: direction error if the direction is not found in the direction list
        """

        if direction in DIRECTIONS:
            self.__current_direction = direction
        else:
            raise DirectionError("Where on earth are you facing?")

    def place(self, x, y, direction):
        self.current_x_coordinate = x
        self.current_y_coordinate = y
        self.current_direction = direction

    def move(self):
        movement_map = {"North": (0, 1),
                        "East":  (1, 0),
                        "South": (0, -1),
                        "West": (-1, 0)}
        movement = movement_map[self.current_direction]
        self.current_x_coordinate = self.current_x_coordinate + movement[0]
        self.current_y_coordinate = self.current_y_coordinate + movement[1]

    def left(self):
        index = DIRECTIONS.index(self.current_direction) + 1
        self.current_direction = DIRECTIONS[index % 4]

    def right(self):
        index = DIRECTIONS.index(self.current_direction) - 1
        self.current_direction = DIRECTIONS[index]

    def report(self):
        return ("Output: %s,%s,%s" % (self.current_x_coordinate, self.current_y_coordinate,
                                      self.current_direction))
