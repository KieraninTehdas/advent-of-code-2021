import sys
from typing import List
from pprint import pprint
import itertools


class BoardElement:
    def __init__(self, number: int):
        self.number = number
        self.is_marked = False

    def mark(self):
        self.is_marked = True

class BingoBoard:
    def __init__(self, board_lines: List[List[int]]):
        self.rows = board_lines
        self.n_rows = len(board_lines)
        self.n_columns = len(board_lines[0])
        self.marked_rows = [[False for _ in range(0, self.n_columns)] for _ in range(0, self.n_rows)]
        pprint(self.marked_rows)


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


def parse_boards(filename: str) -> List[BingoBoard]:
    boards = []
    board = []
    board_lines = [line for line in open(filename, "r")]

    for line_number, line in enumerate(board_lines):
        board_line = [int(component) for component in line.strip().split(" ") if component != ""]

        if not board_line :
            boards.append(BingoBoard(board))
            board = []
            continue
        elif line_number == len(board_lines) - 1:
            board.append(board_line)
            boards.append(BingoBoard(board))
            continue

        board.append(board_line)

    return boards

if __name__ == "__main__":

    boards_file = sys.argv[1]
    numbers_file = sys.argv[2]

    boards = parse_boards(boards_file)

    numbers = [13, 2, 9, 10, 12, 15]

    winner = None

    for number in numbers:
        if winner:
            pprint("We have a winner!")
            pprint(winner.rows)
            break

        print(f"Number is: {number}")

        for board in boards:
            board.mark_number_if_present(number)
            if board.is_complete():
                winner = board
                break
