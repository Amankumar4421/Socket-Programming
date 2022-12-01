# client Side

import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(('192.168.0.102',9999)) # Server Ip Address

while True:
    name = input("Enter Here : ")
    c.send(name.encode())
    if name == "exit":
        break
    reply = c.recv(1024).decode()
    print("Reply : ",reply)

print("Connection Closed")