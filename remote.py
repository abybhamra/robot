"""Class to represent the remote controller
"""
from robot import Robot

DIRECTIONS = ["North", "West", "South", "East"]


class Remote(object):

    def __init__(self):
        self.robot = Robot()

    def place(self, x, y, direction):
        self.robot.place(x, y, direction)

    def move(self):
        # Use Switch Case
        if self.robot.current_direction == "North":
            self.robot.current_y_coordinate += 1
        elif self.robot.current_direction == "East":
            self.robot.current_x_coordinate += 1
        elif self.robot.current_direction == "South":
            self.robot.current_y_coordinate -= 1
        elif self.robot.current_direction == "West":
            self.robot.current_x_coordinate -= 1

    def left(self):
        index = DIRECTIONS.index(self.robot.current_direction) + 1
        self.robot.current_direction = DIRECTIONS[index % 4]

    def right(self):
        index = DIRECTIONS.index(self.robot.current_direction) - 1
        self.robot.current_direction = DIRECTIONS[index]

    def report(self):
        return ("Output: %s,%s,%s" % (self.robot.current_x_coordinate, self.robot.current_y_coordinate,
                                      self.robot.current_direction))
