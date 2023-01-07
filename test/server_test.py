
# tcp_echo_server.py
import socket

ADDRESS = '127.0.0.1'
PORT = 54321

connections = []
host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host.setblocking(0)
host.bind((ADDRESS, PORT))
host.listen(10)  # 10 is how many clients it accepts

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
    for i in reversed(range(len(connections))):
        try:
            data, sender = connections[i][0].recvfrom(1500)
            return data
        except (BlockingIOError, socket.timeout, OSError):
            pass
        except (ConnectionResetError, ConnectionAbortedError):
            close_socket(connections[i][0])
            connections.pop(i)
    return b''  # return empty if no data found

def write(data):
    for i in reversed(range(len(connections))):
        try:
            connections[i][0].sendto(data, connections[i][1])
        except (BlockingIOError, socket.timeout, OSError):
            pass
        except (ConnectionResetError, ConnectionAbortedError):
            close_socket(connections[i][0])
            connections.pop(i)

# Run the main loop
while True:
    try:
        con, addr = host.accept()
        connections.append((con, addr))
    except BlockingIOError:
        pass

    data = read()
    if data != b'':
        print(data)
        write(b'ECHO: ' + data)
        if data == b"exit":
            break

# Close the sockets
for i in reversed(range(len(connections))):
    close_socket(connections[i][0])
    connections.pop(i)
close_socket(host)