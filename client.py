import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISSCONNECT_MESSAGE = '!DISCONNECT'
##SERVER = '192.168.161.1'
#SERVER = '192.168.0.239'
SERVER = '142.93.167.174'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    return client.recv(2048).decode(FORMAT)

def recv():
    return client.recv(2048).decode(FORMAT)

def dissconnect():
    send(DISSCONNECT_MESSAGE)
