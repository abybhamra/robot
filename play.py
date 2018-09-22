# !/usr/bin/env python

from remote import Remote
from robot_exceptions import RobotPlacementError


def main(command):
    players_remote = Remote()
    try:
        players_remote.__setattr__(command, command)
    except RobotPlacementError:
        pass


if __name__ == "__main__":
    main()
