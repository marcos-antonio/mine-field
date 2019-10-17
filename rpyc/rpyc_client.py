import rpyc

class Props:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.drawer = None
        self.cleanFields = []
        self.lastMessageCode = None
        self.proxy = None
props = Props()

def client():
    config = {'allow_public_attrs': True}
    props.proxy = rpyc.connect('localhost', 18861, config=config)

    cant = props.proxy.root.printer('CAN U DO THIS')
    print(cant)

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