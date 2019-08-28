import random


class MineField:
    def __init__(self, rows, cols, nBombs):
        rows = rows if rows >= 4 else 4
        cols = cols if cols >= 5 else 5
        self.field = [list(range(rows)), list(range(cols))]
        self.nBombs = nBombs if nBombs > 5 else 5
        self.bombsPositions = []
        self.__set_bombs_positions__()

    def __set_bombs_positions__(self):
        count = 0
        while (count < self.nBombs):
            posX = random.randint(0, len(self.field[0]))
            posY = random.randint(0, len(self.field[1]))
            hasBomb = False
            for pos in self.bombsPositions:
                hasBomb = pos[0] == posX and pos[1] == posY
            if (hasBomb):
                continue
            self.bombsPositions.append([posX, posY])
            count = count + 1


if __name__ == "__main__":
    mf = MineField(5,5,5)