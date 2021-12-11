import sys
import statistics
from itertools import chain
from pprint import pprint
from typing import List
import math


def calculate_fuel_cost(starting_position: int, final_position: int) -> float:
    displacement = abs(starting_position - final_position)

    return (displacement * (displacement + 1)) / 2

def find_constant_optimum_fuel_cost(x_positions: List[int]) -> float:
    median_position = statistics.median(x_positions)

    return sum([abs(p - median_position) for p in x_positions])

def find_linear_optimum_fuel_cost(x_positions: List[int]):
    mean_position = statistics.mean(x_positions)

    min_mean = int(mean_position)
    max_mean = math.ceil(mean_position)

    if min_mean == max_mean:
        return sum([calculate_fuel_cost(p, max_mean) for p in x_positions])
    else:
        return min([sum([calculate_fuel_cost(p, mean) for p in x_positions]) for mean in [min_mean, max_mean]])

if __name__ == "__main__":
    filename = sys.argv[1]

    x_positions = [
        int(p.strip())
        for p in chain.from_iterable([line.split(",") for line in open(filename, "r")])
    ]

    pprint(find_linear_optimum_fuel_cost(x_positions))
