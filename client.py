import socket

HOST = "192.168.0.43"  # The server's hostname or IP address
PORT = 1234  # The port used by the server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

while True:
    data = server.recv(1024)

    if not data:
        break

    print(f"Received {data.decode('utf-8')!r}")


