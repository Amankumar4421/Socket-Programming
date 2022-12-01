import socket

s_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s_socket.bind(("localhost",9999))

s_socket.listen()

while True:
    print("Server Waiting for Connection...")
    c_socket,addr = s_socket.accept()
    print("Connected with ",addr)
    while True:
        data = c_socket.recv(1024).decode("utf-8")
        if not data or data == 'exit':
            break
        print("From client : ",data)
        
    c_socket.close()
