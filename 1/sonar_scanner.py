import sys

if __name__ == "__main__":
    input_filename = sys.argv[1]

    previous_reading = None
    number_of_increased_readings = 0

    for sonar_reading in open(input_filename, "r"):
        sonar_reading = int(sonar_reading)

        if previous_reading and sonar_reading > previous_reading:
            number_of_increased_readings += 1

        previous_reading = sonar_reading

    print(number_of_increased_readings)
