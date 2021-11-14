import socket
from os import system, name

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONECT"
SERVER = "192.168.56.1"
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
    print(client.recv(2048).decode(FORMAT))


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    exit = False
    while not exit:
        _msg = input("Escribe tu mensaje(0 para salir):")
        if(_msg == "0"):
            exit = True
        else:
            clear()
            send(_msg)

    send(DISCONNECT_MESSAGE)


if __name__ == "__main__":
    main()

