import sys
from typing import List
from pprint import pprint


class BingoBoard:
    def __init__(self, board_lines: List[List[int]]):
        self.board_lines = board_lines
        self.dimensions = (len(board_lines[0]), len(board_lines))

    def contains(self, number: int):
        for line in self.board_lines:
            if number in line:
                return True
            else:
                continue
        
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

    [print(board.contains(1)) for board in boards]
