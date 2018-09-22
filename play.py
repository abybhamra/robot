# !/usr/bin/env python

from robot import Robot
from robot_exceptions import RobotPlacementError


def main(command):
    players_robot = Robot()
    try:
        players_robot.__setattr__(command, command)
    except RobotPlacementError:
        pass


if __name__ == "__main__":
    main()
