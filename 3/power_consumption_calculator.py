import sys
from collections import defaultdict
from operator import itemgetter
from typing import Callable


def calculate_gamma_rate(bit_value_counts: dict) -> int:
    return _calculate_rate(bit_value_counts, max)


def calculate_epsilon_rate(bit_value_counts: dict) -> int:
    return _calculate_rate(bit_value_counts, min)


def _calculate_rate(bit_value_counts: dict, count_evaluator: Callable) -> int:
    components = [
        (x[0], count_evaluator(x[1], key=x[1].get)) for x in bit_value_counts.items()
    ]
    sorted_components = [x for x in sorted(components, key=itemgetter(0))]
    binary_value = "".join([str(x[1]) for x in sorted_components])
    return int(binary_value, 2)


if __name__ == "__main__":
    filename = sys.argv[1]

    bit_value_counts_by_position = defaultdict(lambda: defaultdict(lambda: 0))

    for line in open(filename, "r"):
        line = line.strip()
        for i in range(0, len(line)):
            bit_value_counts_by_position[i][int(line[i])] += 1

    power_consumption = calculate_epsilon_rate(
        bit_value_counts_by_position
    ) * calculate_gamma_rate(bit_value_counts_by_position)

    print(power_consumption)
