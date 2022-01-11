import numpy as np


class Board:

    def __init__(self, data):
        self.data = data
        self.marked = np.zeros((5, 5))

    def mark(self, num):
        for i in range(5):
            for j in range(5):
                if self.data[i][j] == num:
                    self.marked[i, j] = 1

    def won(self):
        for i in range(5):
            win = True
            for j in range(5):
                if self.marked[i, j] == 0:
                    win = False
            if win:
                return True

        for j in range(5):
            win = True
            for i in range(5):
                if self.marked[i, j] == 0:
                    win = False
            if win:
                return True
        return False

    def score(self, called):
        score = 0
        for i in range(5):
            for j in range(5):
                if self.marked[i, j] == 0:
                    score += self.data[i][j]
        return score * called


lines = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        if not line.isspace():
            lines.append(line.split('\n')[:-1])

rands = lines[0]
rands = list(map(int, (rands[0]).split(",")))
lines = lines[1:]

boards = []
for i in range(0, len(lines), 5):
    this_board = []
    for j in range(5):
        a = list(map(int, lines[j+i][0].strip().split()))
        this_board.append(a)
    boards.append(Board(this_board))

for r in rands:
    for board in boards:
        board.mark(r)
        if board.won():
            print(board.score(r))
            exit()

