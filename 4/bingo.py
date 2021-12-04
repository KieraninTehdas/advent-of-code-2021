import sys
from typing import List
from pprint import pprint
import itertools


class BingoBoard:
    def __init__(self, board_lines: List[List[int]]):
        self.rows = board_lines
        self.n_rows = len(board_lines)
        self.n_columns = len(board_lines[0])
        self.marked_rows = [
            [False for _ in range(0, self.n_columns)] for _ in range(0, self.n_rows)
        ]

    def _find_index_of(self, number: int):
        for row_number, row in enumerate(self.rows):
            try:
                return (row_number, row.index(number))
            except ValueError:
                continue

        return None

    def mark_number_if_present(self, number: int):
        index_of_number = self._find_index_of(number)

        if not index_of_number:
            return

        self.marked_rows[index_of_number[0]][index_of_number[1]] = True

    def is_complete(self):
        return self._has_complete_row() or self._has_complete_column()

    def _has_complete_row(self):
        return self._all_marked(self.marked_rows)

    def _has_complete_column(self):
        marked_columns = [[] for _ in range(0, self.n_columns)]
        for row in self.marked_rows:
            for column_number, marked_value in enumerate(row):
                marked_columns[column_number].append(marked_value)

        return self._all_marked(marked_columns)

    @staticmethod
    def _all_marked(marked_values: List[List[bool]]) -> bool:
        for row in marked_values:
            if row[0] is True and len(set(row)) == 1:
                return True

        return False

    def sum_of_unmarked_elements(self):
        unmarked_numbers = []
        for row_number, row in enumerate(self.marked_rows):
            unmarked_numbers.extend(
                [
                    self.rows[row_number][column_number]
                    for column_number, is_marked in enumerate(row)
                    if not is_marked
                ]
            )

        return sum(unmarked_numbers)


def parse_boards(filename: str) -> List[BingoBoard]:
    boards = []
    board = []
    board_lines = [line for line in open(filename, "r")]

    for line_number, line in enumerate(board_lines):
        board_line = [
            int(component) for component in line.strip().split(" ") if component != ""
        ]

        if not board_line:
            boards.append(BingoBoard(board))
            board = []
            continue
        elif line_number == len(board_lines) - 1:
            board.append(board_line)
            boards.append(BingoBoard(board))
            continue

        board.append(board_line)

    return boards


def find_first_winner(boards: List[BingoBoard], numbers: List[int]):
    winner = None

    previous_number = None

    for number in numbers:
        if winner:
            pprint("We have a winner!")
            pprint(winner.rows)

            print(
                f"Winning score: {winner.sum_of_unmarked_elements() * previous_number}"
            )
            break

        previous_number = number

        for board in boards:
            board.mark_number_if_present(number)
            if board.is_complete():
                winner = board
                break

    if not winner:
        print("No one won :(")


def find_last_loser(boards: List[BingoBoard], numbers: List[int]):
    incomplete_boards = [board for board in boards]

    previous_number = None

    for number in numbers:

        previous_number = number

        complete_board_indices = []
        for idx, board in enumerate(incomplete_boards):
            board.mark_number_if_present(number)
            if board.is_complete():
                complete_board_indices.append(idx)

        is_last_completed_board = (
            len(incomplete_boards) == 1 and len(complete_board_indices) == 1
        )

        if is_last_completed_board:
            loser = incomplete_boards[0]

            pprint("We have a loser!")
            pprint(loser.rows)
            print(f"Losing score {loser.sum_of_unmarked_elements() * previous_number}")
            break

        incomplete_boards = [
            board
            for idx, board in enumerate(incomplete_boards)
            if idx not in complete_board_indices
        ]


if __name__ == "__main__":

    boards_file = sys.argv[1]
    numbers_file = sys.argv[2]

    boards = parse_boards(boards_file)

    numbers = [
        int(number)
        for number in itertools.chain.from_iterable(
            [line.strip().split(",") for line in open(numbers_file, "r")]
        )
    ]

    find_first_winner(boards, numbers)
    find_last_loser(boards, numbers)
