import socket
import re


def get_addr_server():
    try:
        print("Enter Server address")
        addr_server = input()
        socket.inet_aton(addr_server)
    except:
        print("Invalid format address")
        get_addr_server()
    return addr_server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    addr_server = get_addr_server()
    s.connect((addr_server, 1303))
    print("Connection Succesfull")
    data = s.recv(1024)
    print(data)
