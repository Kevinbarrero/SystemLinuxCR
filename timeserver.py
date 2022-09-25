import socket
from datetime import datetime

# define socket type and arguments
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
addr = ("0.0.0.0", 1303)
# add 'name' and port for this socket.
s.bind(addr)


def socket_server():
    # listen for a client
    s.listen()
    client = s.accept()
    ##save client's socket
    client_s = client[0]
    print(client_s)
    # send message to client from server
    date = datetime.today().strftime("%d-%m-%Y %H:%M")
    client_s.send(date.encode())


if __name__ == "__main__":
    # creating thread
    while True:
        socket_server()
