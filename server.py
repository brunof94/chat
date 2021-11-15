import socket
import threading
from datetime import datetime


chat_history = "CHAT HISTORY \n"
names = ""
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected. \n")
    global chat_history
    global names
    _name = ""
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            if _name != "":
                _msg = f"[{addr}][{_name}]:  {msg}"
                print(_msg)
                chat_history = chat_history + f"[{datetime.now().strftime('%X')}]:" + _msg + "\n"
            else:
                _name = msg
                names += f"[{addr}]-[{_name}]"
                chat_history = chat_history + f"[{datetime.now().strftime('%X')}]: {_name} has joined the chat \n"
            conn.send(chat_history.encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting")
start()
