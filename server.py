import socket
from datetime import datetime
from mine-field import MineField

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = ''
userlist = {}
orig = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(orig)

board

def server():
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        data = data.decode(ENCODE).split(':')
        responseCode = '2'
        messageCode = '0'
        action = data[0]
        rows, cols, nBombs = data[1].split(',').split()

        if (action == '1'):
            board = MineField(rows, cols, nBombs)
            responseCode = '1'
            messageCode = '5'
        elif (action == '2'):
            responseCode = 2
            responseAction = 2
            text = str(list(userlist.keys()))
        elif (action == '3'):
            responseAction = 1
            if sendMessage(data[0], data[1]) == True:
                responseCode = 2
                text = 'Mensagem enviada'
            else:
                responseCode = 4
                text = 'Usuario nao encontrado'
        sock.sendto(f'{responseCode}:{messageCode}'.encode(ENCODE), address)


def registerUser(username, data):
    if userlist.get(username) == None:
        userlist[username] = data
        return True
    else:
        return False

def sendMessage(message, destiny):
    destinyAddress = userlist.get(destiny)
    if destinyAddress == None:
        return False
    else:
        message = ('2:' + message + ':3').encode(ENCODE)
        sock.sendto(message, destinyAddress)
        return True

server()