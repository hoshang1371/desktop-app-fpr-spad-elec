# tcp_client.py
import socket

ADDRESS = "localhost"
PORT = 54321

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, PORT))
s.setblocking(0)

def close_socket(connection):
    try:
        connection.shutdown(socket.SHUT_RDWR)
    except:
        pass
    try:
        connection.close()
    except:
        pass

def read():
    """Read data and return the read bytes."""
    try:
        data, sender = s.recvfrom(1500)
        return data
    except (BlockingIOError, socket.timeout, AttributeError, OSError):
        return b''
    except (ConnectionResetError, ConnectionAbortedError, AttributeError):
        close_socket(s)
        return b''

def write(data):
    try:
        s.sendto(data, (ADDRESS, PORT))
    except (ConnectionResetError, ConnectionAbortedError):
        close_socket(s)

while True:
    msg = input("Enter a message: ")
    write(msg.encode('utf-8'))

    data = read()
    if data != b"":
        print("Message Received:", data)

    if msg == "exit":
        break

close_socket(s)