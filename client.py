import socket
from os import system, name

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONECT"
SERVER = "127.0.1.1"
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
    _exit = False
    _name = ""
    while not _exit:
        if _name != "":
            _msg = input("Escribe tu mensaje(0 para salir):")
        else:
            _msg = input("Escribe tu nombre(0 para salir):")
            _name = _msg
        if _msg == "0":
            _exit = True
            send(DISCONNECT_MESSAGE)
        else:
            clear()
            print(_name)
            send(_msg)


if __name__ == "__main__":
    main()

