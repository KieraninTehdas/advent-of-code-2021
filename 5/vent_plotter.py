import sys
from pprint import pprint
from typing import List, NamedTuple
from collections import defaultdict


class Point(NamedTuple):
    x: int
    y: int


class LineSegment:
    def __init__(self, starting_point: Point, ending_point: Point):
        self.starting_point = starting_point
        self.ending_point = ending_point

    def is_axis_parallel_line(self):
        return (
            self.starting_point.x == self.ending_point.x
            or self.starting_point.y == self.ending_point.y
        )

    def construct_line_points(self) -> List[Point]:
        if self.starting_point.x == self.ending_point.x:
            step = -1 if self.starting_point.y > self.ending_point.y else 1
            stop = self.ending_point.y - 1 if step < 0 else self.ending_point.y + 1

            return [
                Point(x=self.starting_point.x, y=y_value)
                for y_value in range(self.starting_point.y, stop, step)
            ]
        elif self.starting_point.y == self.ending_point.y:
            step = -1 if self.starting_point.x > self.ending_point.x else 1
            stop = self.ending_point.x - 1 if step < 0 else self.ending_point.x + 1

            return [
                Point(x=x_value, y=self.starting_point.y)
                for x_value in range(self.starting_point.x, stop, step)
            ]
        else:
            return []


if __name__ == "__main__":
    input_filename = sys.argv[1]

    grid_points = defaultdict(lambda: 0)

    for line in open(input_filename, "r"):
        starting_point, ending_point = [
            Point(x=int(component[0]), y=int(component[1]))
            for component in [
                coordinate.strip().split(",") for coordinate in line.split("->")
            ]
        ]

        line_segment = LineSegment(
            starting_point=starting_point, ending_point=ending_point
        )

        if line_segment.is_axis_parallel_line():
            for point in line_segment.construct_line_points():
                grid_points[point] += 1

    n_overlap_points = sum(1 for count in grid_points.values() if count > 1)

    pprint(f"Beware! There are {n_overlap_points} overlap points!")
