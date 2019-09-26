import socket
import threading
from datetime import datetime
from drawer import Drawer

ENCODE = "UTF-8"
HOST = '127.0.0.1'
PORT = 5000
MAX_BYTES = 65535
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverDest = (HOST, PORT)

rows = 0
cols = 0
drawer = None
cleanFields = []

def client():
    registerBoardInfo()
    drawer = Drawer([list(range(rows)), list(range(cols))])
    waitForCommands()

def waitForCommands():
    while True:
        drawer.draw(self, cleanFields)
        x = str(input('Type in a value for the X axis: '))
        y = str(input('Type in a value for the Y axis: '))
        selectPos(x, y)

def registerBoardInfo():
    isAccepted = False
    while isAccepted == False:
        uRows = str(input('Type in the number of rows for this game:\n'))
        uCols = str(input('Type in the number of columns for this game:\n'))
        nBombs = str(input('Type in the number of bombs for this game:\n'))

        encodedStr = str('1:' + uRows + ',' + uCols + ',' + nBombs).encode(ENCODE)

        sock.sendto(encodedStr, serverDest)

        data, address = sock.recvfrom(MAX_BYTES)
        response = data.decode(ENCODE).split(':')

        isAccepted = response[0] == '1'
        rows = uRows
        cols = uCols
    return None

def selectPos(x, y):
    encodedStr = str('2:' + x + ',' + y).encode(ENCODE)

    sock.sendto(encodedStr, serverDest)
    data, address = sock.recvfrom(MAX_BYTES)
    response = data.decode(ENCODE).split(':')
    print(response[1])

client()