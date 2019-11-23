import sys
sys.path.insert(1, '../')
import zmq
import time
import sys
import random

from minefield import MineField

try:
    port = "5560"
    ENCODE = "UTF-8"
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect("tcp://localhost:%s" % port)
    server_id = random.randrange(1,10005)
    while True:
        data = socket.recv()
        data = data.decode(ENCODE).split(':')
        responseCode = '2'
        messageCode = '0'
        action = data[0]

        if (action == '1'):
            rows, cols, nBombs = data[1].split(',')
            board = MineField(int(rows), int(cols), int(nBombs))
            responseCode = '1'
            messageCode = '5'
        elif (action == '2'):
            x, y = data[1].split(',')
            messageCode = board.selectPos(int(x), int(y))
            if (board.areAllPositionsCleared()):
                messageCode = 6
        print(f'bombs positions: {board.bombsPositions}')
        socket.send(f'{responseCode}:{messageCode}:{board.positionsCleared}'.encode(ENCODE))
except:
    for val in sys.exc_info():
        print(val)