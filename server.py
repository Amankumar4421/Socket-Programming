# Server Side

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")

s.bind(('192.168.0.102',9999))  # Server Ip Address
print("Binded")

s.listen(2)

while True:
    print("Waiting for Connection...")
    conn,addr=s.accept()
    print("Connected with : ",addr)
    while True:
        name = conn.recv(1024).decode()
        if name == "exit":
            break
        print("From Client : ",name)
        abc = input("Enter Reply : ")
        conn.send(bytes(abc,'utf-8'))
    conn.close()
    print("Connection Closed with : ",addr)