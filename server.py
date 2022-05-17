import socket
import serial
import time

HOST = "192.168.0.43"
PORT = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
arduino = serial.Serial(port='COM9', baudrate=9600, timeout=.1)
client, addr = server.accept()

print(f"Server Started at {HOST}:{PORT}")
print(f"Connected with client {client}")


def write_read():
    data = arduino.readline()
    return data


while True:
    value = write_read()
    message = str(value).encode('utf-8')
    client.send(message)
