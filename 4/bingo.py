import sys
from pprint import pprint

if __name__ == "__main__":

    boards_file = sys.argv[1]
    numbers_file = sys.argv[2]

    boards = []
    board = []

    for line in open(boards_file, "r"):
        board_line = [component for component in line.strip().split(" ") if component != ""]
        pprint(board_line)

        if not board_line:
            boards.append(board)
            board = []
            print("Bail out")
            continue

        board.append(board_line)

    pprint(boards)
    print(len(boards))

