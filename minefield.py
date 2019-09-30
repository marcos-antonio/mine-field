import random
from drawer import Drawer

class MineField:
    def __init__(self, rows, cols, nBombs):
        self.rows = rows
        self.cols = cols
        self.nBombs = nBombs
        self.board = [list(range(rows)), list(range(cols))]
        self.bombsPositions = []
        self.positionsCleared = []
        self.__set_bombs_positions__()
        self.isOver = False

    def __set_bombs_positions__(self):
        count = 0
        while (count < self.nBombs):
            posX = random.randint(0, len(self.board[0]) - 1)
            posY = random.randint(0, len(self.board[1]) - 1)
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
            if (pos[0][0] == x and pos[0][1] == y):
                return True
        return False

    def __pos__exists(self, x, y):
        return x >= 0 and y >= 0 and x < len(self.board[0]) and y < len(self.board[1])

    def selectPos(self, x, y, rec=False):
        if (not self.__pos__exists(x, y)):
            return 2
        if (self.__pos_has_bomb__(x, y)):
            return 3
        if (self.__pos_is_clear(x, y)):
            return 4
        nearbyBombs = self.__get_nearby_bombs__(x, y)
        self.positionsCleared.append([[x, y], nearbyBombs])
        if (nearbyBombs == 0 and not rec):
            self.__clear_neighbours__(x, y)
        return 1

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
                if (y == i and k == x):
                    continue
                self.selectPos(k, i, True)

    def areAllPositionsCleared(self):
        return len(self.positionsCleared) == (self.rows * self.cols) - self.nBombs



def displayMessage(code):
    if (code == 1):
        print('Selected position was cleared')
    elif (code == 2):
        print('Position does not exists')
    elif (code == 3):
        print('You stepped on a bomb, game over')
    elif (code == 4):
        print('Position already clear')
    elif (code == 6):
        print('You won')

if __name__ == "__main__":
    uRows = int(input('Type in the number of rows for this game:\n'))
    uCols = int(input('Type in the number of columns for this game:\n'))
    nBombs = int(input('Type in the number of bombs for this game:\n'))
    mf = MineField(uRows, uCols, nBombs)
    dw = Drawer(mf.board)
    while (not mf.isOver):
        dw.draw(mf.positionsCleared)
        x = int(input('Type in a value for the X axis: '))
        y = int(input('Type in a value for the Y axis: '))
        code = mf.selectPos(x, y)
        displayMessage(code)
        if (code in (3, 6)):
            mf.isOver = True
            dw.draw(mf.positionsCleared)
