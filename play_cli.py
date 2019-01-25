# play_cli.py
import sys

import click

import robot_exceptions
from robot import Robot


@click.group(invoke_without_command=True)
@click.option("--x", prompt="Robots X coordinate", help="The Robots X coordinate. Type = int")
@click.option("--y", prompt="Robots Y coordinate", help="The Robots Y coordinate. Type = int")
@click.option("--direction", prompt="Robots direction", help="The Robots direction. sample West, South, East, North")
@click.pass_context
def robo_cli(ctx, x, y, direction):
    robot = Robot(int(x), int(y), direction)
    ctx.obj = robot

    if ctx.invoked_subcommand is None:
        run_multiple_commands(robot)


def run_multiple_commands(robot):
    while True:
        cmd = get_command_line_input()
        validate_robot_command(cmd, robot)
        execute_robot_command(cmd, robot)


def get_command_line_input():
    return input("Command: ")


def validate_robot_command(cmd, robot):
    if cmd not in dir(robot):
        click.echo("Invalid command: " + cmd)
        sys.exit(1)


def execute_robot_command(cmd, robot):
    try:
        robot.__getattribute__(cmd)()
        click.echo("Current Position: " + robot.report())
    except robot_exceptions.RobotError as e:
        click.echo("Failed. Reason: " + e.message)
        sys.exit(1)


@robo_cli.command()
@click.pass_obj
def move(robot):
    robot.move()


@robo_cli.command()
@click.pass_obj
def left(robot):
    robot.left()


@robo_cli.command()
@click.pass_obj
def right(robot):
    robot.right()


@robo_cli.command()
@click.pass_obj
def report(robot):
    print(robot.report())


if __name__ == "__main__":
    robo_cli()
