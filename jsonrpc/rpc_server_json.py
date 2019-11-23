import sys
sys.path.insert(1, '../')
from minefield import MineField

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

board = None

def create_mine_field(rows, cols, nBombs):
    global board
    board = MineField(int(rows), int(cols), int(nBombs))
    return 1

def play_on_coordinates(x, y):
    print(board)
    messageCode = board.selectPos(x,y)
    if (board.areAllPositionsCleared()):
        return 6
    return messageCode

def get_positions_cleared():
    return board.positionsCleared

def server():
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(create_mine_field)
    serverRPC.register_function(play_on_coordinates)
    serverRPC.register_function(get_positions_cleared)
    print("Starting server")
    serverRPC.serve_forever()