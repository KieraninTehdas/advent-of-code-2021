import sys
import statistics
from itertools import chain
from pprint import pprint

if __name__ == "__main__":
    filename = sys.argv[1]

    x_positions = [
        int(p.strip())
        for p in chain.from_iterable([line.split(",") for line in open(filename, "r")])
    ]

    median_position = statistics.median(x_positions)

    fuel_cost = sum([abs(p - median_position) for p in x_positions])

    pprint(fuel_cost)
