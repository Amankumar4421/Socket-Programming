import socket

c_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    name = input("Enter to Send : ")
    if name == 'exit':
        break
    c_socket.sendto(name.encode('utf-8'),("localhost",9999))

c_socket.close()