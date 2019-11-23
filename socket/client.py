import sys
sys.path.insert(1, '../')
import socket
import threading
from datetime import datetime
from drawer import Drawer

class Props:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.drawer = None
        self.cleanFields = []
        self.lastMessageCode = None

ENCODE = "UTF-8"
HOST = '127.0.0.1'
PORT = 5000
MAX_BYTES = 65535
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverDest = (HOST, PORT)

props = Props()

def client():
    registerBoardInfo()
    props.drawer = Drawer([list(range(int(props.rows))), list(range(int(props.cols)))])
    waitForCommands()

def waitForCommands():
    while props.lastMessageCode != 3 and props.lastMessageCode != 6:
        displayMessage()
        props.drawer.draw(props.cleanFields)
        x = str(input('Type in a value for the X axis: '))
        y = str(input('Type in a value for the Y axis: '))
        selectPos(x, y)

    displayMessage();
    props.drawer.draw(props.cleanFields)

def displayMessage():
    if (props.lastMessageCode == 1):
        print('Selected position was cleared')
    elif (props.lastMessageCode == 2):
        print('Position does not exists')
    elif (props.lastMessageCode == 3):
        print('You stepped on a bomb, game over')
    elif (props.lastMessageCode == 4):
        print('Position already clear')
    elif (props.lastMessageCode == 6):
        print('You won')


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
        props.rows = uRows
        props.cols = uCols

def selectPos(x, y):
    encodedStr = str('2:' + x + ',' + y).encode(ENCODE)

    sock.sendto(encodedStr, serverDest)
    data, address = sock.recvfrom(MAX_BYTES)
    response = data.decode(ENCODE).split(':')
    props.cleanFields = eval(response[2])
    props.lastMessageCode = int(response[1])

client()