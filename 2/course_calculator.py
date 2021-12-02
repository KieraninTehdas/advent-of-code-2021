import sys
from typing import NamedTuple

class CourseAction(NamedTuple):
    magnitude: int
    direction: str

class Position(NamedTuple):
    x: int
    y: int


def move_forward(starting_position: Position, magnitude: int) -> Position:
    return Position(x=starting_position.x + magnitude, y=starting_position.y)

def move_backward(starting_position: Position, magnitude: int) -> Position:
    return Position(starting_position.x - magnitude, y=starting_position.y)

def move_down(starting_position: Position, magnitude: int) -> Position:
    return Position(x=starting_position.x, y=starting_position.y + magnitude)

def move_up(starting_position: Position, magnitude: int) -> Position:
    return Position(x=starting_position.x, y=starting_position.y - magnitude)

COURSE_DIRECTION_RESULTS = {
        "forward": move_forward,
        "backward": move_backward,
        "up": move_up,
        "down": move_down
        }


def parse_course_action(line: str) -> CourseAction:
    course_action = line.strip().split(" ")

    if len(course_action) != 2:
        raise ValueError(f"Invalid course action {line}")

    return CourseAction(magnitude=int(course_action[1]), direction=course_action[0].lower())


if __name__ == "__main__":
    filename = sys.argv[1]

    position = Position(0, 0)

    for line in open(filename, "r"):
        course_action = parse_course_action(line)
        position = COURSE_DIRECTION_RESULTS[course_action.direction](position, course_action.magnitude)

    print(position.x * position.y)

