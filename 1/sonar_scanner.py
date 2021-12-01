import sys
from collections import deque


def calculate_simple_reading_increase_frequency(filename: str):
    previous_reading = None
    number_of_increased_readings = 0

    for sonar_reading in open(filename, "r"):
        sonar_reading = int(sonar_reading)

        if previous_reading and sonar_reading > previous_reading:
            number_of_increased_readings += 1

        previous_reading = sonar_reading

    return number_of_increased_readings


def calculate_sliding_window_increase_frequency(filename: str, window_length: int = 3):
    number_of_increased_readings = 0
    previous_window_sum = None
    window = deque([], maxlen=window_length)

    for sonar_reading in open(filename, "r"):
        window.append(int(sonar_reading))

        if len(window) == window_length:
            window_sum = sum(window)

            if previous_window_sum and window_sum > previous_window_sum:
                number_of_increased_readings += 1

            previous_window_sum = window_sum

    return number_of_increased_readings


if __name__ == "__main__":
    input_filename = sys.argv[1]

    result = calculate_sliding_window_increase_frequency(input_filename)

    print(result)
