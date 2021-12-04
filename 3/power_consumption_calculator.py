import sys
from collections import defaultdict
from operator import itemgetter
from typing import Callable, List
from itertools import count
from statistics import multimode


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


def calculate_power_consumption(bit_value_counts: dict) -> int:
    return calculate_gamma_rate(bit_value_counts) * calculate_epsilon_rate(
        bit_value_counts
    )


def _calculate_oxygen_rating_criteria(bit_values: List[int]) -> int:
    most_common_bit_values = multimode(bit_values)

    if len(most_common_bit_values) > 1:
        criteria = 1
    else:
        criteria = most_common_bit_values[0]

    return criteria


def calculate_oxygen_generator_rating(diagnostic_values: List[str]) -> int:
    return _calculate_rating(diagnostic_values, _calculate_oxygen_rating_criteria)


def _calculate_co2_rating_criteria(bit_values: List[int]) -> int:
    bit_value_frequencies = defaultdict(lambda: 0)

    for value in bit_values:
        bit_value_frequencies[value] += 1

    if bit_value_frequencies[0] == bit_value_frequencies[1]:
        criteria = 0
    else:
        criteria = min(bit_value_frequencies, key=bit_value_frequencies.get)

    return criteria


def calculate_co2_scrubber_rating(diagnostic_values: List[str]) -> int:
    return _calculate_rating(diagnostic_values, _calculate_co2_rating_criteria)


def _calculate_rating(reported_values: List[str], criteria_calculator: Callable) -> int:
    matching_values = reported_values

    for i in count():
        if len(matching_values) == 1:
            return int(matching_values[0], 2)

        try:
            bit_values_at_position = [int(line[i]) for line in matching_values]
        except IndexError:
            raise RuntimeError("Failed to find a single matching line")

        criteria = criteria_calculator(bit_values_at_position)

        matching_values = [line for line in matching_values if int(line[i]) == criteria]


def calculate_life_support_rating(diagnostic_values: List[str]) -> int:
    return calculate_co2_scrubber_rating(
        diagnostic_values
    ) * calculate_oxygen_generator_rating(diagnostic_values)


if __name__ == "__main__":
    filename = sys.argv[1]

    bit_value_counts_by_position = defaultdict(lambda: defaultdict(lambda: 0))

    diagnostic_values = [line.strip() for line in open(filename, "r")]

    for diagnostic_value in diagnostic_values:
        for i in range(0, len(diagnostic_value)):
            bit_value_counts_by_position[i][int(diagnostic_value[i])] += 1

    print(
        f"Power consumption is {calculate_power_consumption(bit_value_counts_by_position)}"
    )

    print(f"Life support rating is {calculate_life_support_rating(diagnostic_values)}")
