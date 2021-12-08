from __future__ import annotations
import sys
import itertools

DEFAULT_DAYS_TO_RUN = 80


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


def simulate_fish_growth(filename: str):
    fishes = [
        Lanternfish(int(timer.strip()))
        for timer in itertools.chain.from_iterable(
            [line.split(",") for line in open(filename, "r")]
        )
    ]

    n_fish = [len(fishes)]
    for _ in range(0, days_to_run):
        fishes.extend(fish.spawn() for fish in fishes if fish.is_ready_to_spawn())

        for fish in fishes:
            fish.evolve()
        n_fish.append(len(fishes))

    print(f"There are now {len(fishes)} after {days_to_run} days")


if __name__ == "__main__":
    filename = sys.argv[1]
    try:
        days_to_run = int(sys.argv[2])
    except KeyError:
        days_to_run = DEFAULT_DAYS_TO_RUN

    initial_fish_timers = [
        int(timer.strip())
        for timer in itertools.chain.from_iterable(
            [line.split(",") for line in open(filename, "r")]
        )
    ]

    fish_timers = {timer: 0 for timer in range(0, 9)}

    for timer in initial_fish_timers:
        fish_timers[timer] += 1

    for _ in range(0, days_to_run):
        fish_timers = {
            time_to_spawn - 1: n_fish for time_to_spawn, n_fish in fish_timers.items()
        }
        fish_timers[8] = fish_timers[-1]
        fish_timers[6] = fish_timers[6] + fish_timers[-1]
        del fish_timers[-1]

    print(
        f"After {days_to_run} days there are {sum(fish_timers.values())} lantern fish"
    )
