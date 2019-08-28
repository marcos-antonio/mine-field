class Drawer:

    def __init__(self, board):
        self.board = board

    def draw(self, cleanFields):
        for y in self.board[1]:
            for x in self.board[0]:
                ch = '  ' if [x,y] in cleanFields else '* '
                print(ch, end='')
            print('\n')

if __name__ == '__main__':
    dw = Drawer([list(range(5)), list(range(4))]);
    dw.draw([[1,1], [2, 2]])
