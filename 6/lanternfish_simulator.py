from __future__ import annotations
import sys
from pprint import pprint
import itertools

DAYS_TO_RUN = 80


class Lanternfish:
    def __init__(self, days_until_spawn: int):
        self.days_until_spawn = days_until_spawn

    def is_ready_to_spawn(self) -> bool:
        return self.days_until_spawn == 0

    def spawn(self) -> Lanternfish:
        self.days_until_spawn = 7
        return Lanternfish(9)

    def evolve(self):
        self.days_until_spawn -= 1


if __name__ == "__main__":
    filename = sys.argv[1]

    fishes = [
        Lanternfish(int(timer.strip()))
        for timer in itertools.chain.from_iterable(
            [line.split(",") for line in open(filename, "r")]
        )
    ]

    new_fish = []
    for day in range(0, DAYS_TO_RUN):
        fishes.extend(fish.spawn() for fish in fishes if fish.is_ready_to_spawn())

        for fish in fishes:
            fish.evolve()

    print(f"There are now {len(fishes)} after {DAYS_TO_RUN} days")
