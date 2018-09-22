"""
class to set custom exceptions.
"""


class RobotError(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super(RobotError, self).__init__(message)


class DirectionError(RobotError):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super(DirectionError, self).__init__(message)


class RobotPlacementError(RobotError):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super(RobotPlacementError, self).__init__(message)
