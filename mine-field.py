import random
from drawer import Drawer


class MineField:
    def __init__(self, rows, cols, nBombs):
        rows = rows if rows >= 10 else 10
        cols = cols if cols >= 10 else 10
        self.board = [list(range(rows)), list(range(cols))]
        self.nBombs = nBombs if nBombs > 5 else 5
        self.bombsPositions = []
        self.positionsCleared = []
        self.__set_bombs_positions__()
        self.isOver = False

    def __set_bombs_positions__(self):
        count = 0
        while (count < self.nBombs):
            posX = random.randint(0, len(self.board[0]))
            posY = random.randint(0, len(self.board[1]))
            if (self.__pos_has_bomb__(posX, posY)):
                continue
            self.bombsPositions.append([posX, posY])
            count = count + 1

    def __pos_has_bomb__(self, x, y):
        for pos in self.bombsPositions:
            if (pos[0] == x and pos[1] == y):
                return True
        return False

    def __pos_is_clear(self, x, y):
        for pos in self.positionsCleared:
            if (pos[0] == x and pos[1] == y):
                return True
        return False

    def __pos__exists(self, x, y):
        return x >= 0 and y >= 0 and x < len(self.board[0]) and y < len(self.board[1])

    def selectPos(self, x, y, rec=False):
        if (not self.__pos__exists(x, y)):
            return 'Position does not exists'
        if (self.__pos_has_bomb__(x, y)):
            return 'Game Over, you hit a bomb'
        if (self.__pos_is_clear(x, y)):
            return 'Position already clear'
        nearbyBombs = self.__get_nearby_bombs__(x, y)
        self.positionsCleared.append([[x, y], nearbyBombs])
        if (nearbyBombs == 0 and not rec):
            self.__clear_neighbours__(x, y)
        return 'Position cleared'

    def __get_nearby_bombs__(self, x, y):
        topY = y - 1
        leftX = x - 1
        rightX = x + 1
        bottomY = y + 1
        bombCount = 0
        for i in list(range(topY, bottomY + 1)):
            for k in list(range(leftX, rightX + 1)):
                if (y == i and k == x):
                    continue
                if (self.__pos_has_bomb__(k, i)):
                    bombCount = bombCount + 1
        return bombCount

    def __clear_neighbours__(self, x, y, xParent=-1, yParent=- 1):
        topY = y - 1
        leftX = x - 1
        rightX = x + 1
        bottomY = y + 1
        bombCount = 0
        for i in list(range(topY, bottomY + 1)):
            for k in list(range(leftX, rightX + 1)):
                print('Searching for a bomb on: ', k, i)
                if (y == i and k == x):
                    continue
                self.selectPos(k, i, True)


if __name__ == "__main__":
    mf = MineField(5, 5, 5)
    dw = Drawer(mf.board)
    while (not mf.isOver):
        dw.draw(mf.positionsCleared)
        x = int(input('Type in a value for the X axis: '))
        y = int(input('Type in a value for the Y axis: '))
        if (mf.selectPos(x, y) == 'Game Over, you hit a bomb'):
            mf.isOver = True
