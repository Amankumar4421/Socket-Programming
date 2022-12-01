import socket

c_socket = socket.socket()

host = '127.0.0.1'
port = 4421

c_socket.connect((host,port))

respone = c_socket.recv(1024)
print(respone.decode('utf-8'))

while True:
    input = input("Enter data : ")
    c_socket.send(input.encode('utf-8'))
    respone = c_socket.recv(1024)
    print(respone.decode('utf-8'))

c_socket.close()