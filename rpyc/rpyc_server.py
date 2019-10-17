import rpyc
from rpyc.utils.server import ThreadedServer

class MyServer(rpyc.service):

    def __init__(self):
        self.board = None

    def exposed_printer(self, arg):
        print('has called the server printer')
        return 'truedat'
        
    def exposed_create_board(self, rows, cols, nBombs):
        self.board = MineField(int(rows), int(cols), int(nBombs))
        return True

    def exposed_select_pos(self, x, y):
        messageCode = self.board.selectPos(int(x), int(y))
        if (self.board.areAllPositionsCleared()):
            messageCode = 6
        return messageCode

def server():    
    t = ThreadedServer(MyServer, port = 18861)
    t.start()