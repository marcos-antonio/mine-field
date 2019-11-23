import sys
sys.path.insert(1, '../')

from drawer import Drawer
from jsonrpclib import Server


class Props:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.drawer = None
        self.cleanFields = []
        self.lastMessageCode = None


props = Props()
proxy = Server('http://localhost:7002')


def client():
    registerBoardInfo()
    props.drawer = Drawer([list(range(int(props.rows))), list(range(int(props.cols)))])
    waitForCommands()


def registerBoardInfo():
    isAccepted = False
    while isAccepted == False:
        uRows = int(input('Type in the number of rows for this game:\n'))
        uCols = int(input('Type in the number of columns for this game:\n'))
        nBombs = int(input('Type in the number of bombs for this game:\n'))

        isAccepted = proxy.create_mine_field(uRows, uCols, nBombs) == 1

    props.rows = uRows
    props.cols = uCols


def waitForCommands():
    while props.lastMessageCode != 3 and props.lastMessageCode != 6:
        displayMessage()
        props.drawer.draw(props.cleanFields)
        x = int(input('Type in a value for the X axis: '))
        y = int(input('Type in a value for the Y axis: '))
        selectPos(x, y)

    displayMessage();
    props.drawer.draw(props.cleanFields)
    sys.exit()


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

def selectPos(x, y):
    props.lastMessageCode = proxy.play_on_coordinates(x, y)
    props.cleanFields = proxy.get_positions_cleared()