import socket
from datetime import datetime
from minefield import MineField

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = ''
userlist = {}
orig = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(orig)

board = None

def server():
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
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
        sock.sendto(f'{responseCode}:{messageCode}:{board.positionsCleared}'.encode(ENCODE), address)

server()