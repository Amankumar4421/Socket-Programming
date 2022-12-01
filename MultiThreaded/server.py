import socket
from _thread import *
s_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'
port = 4421
threadCount = 0

s_socket.bind((host,port))
s_socket.listen()
print("Waiting for Connection...")

def client_thread(conn):
    conn.send("welcome to ther server".encode('utf-8'))
    while True:
        data = conn.recv(1024)
        reply = "hello "+data.decode('utf-8')
        if not data:
            break
        conn.sendall(reply.encode('utf-8'))
    conn.close()

while True:
    client,addr = s_socket.accept()
    print("Connected with ",addr)
    start_new_thread(client_thread(client))
    threadCount+=1
    print("ThreadCount : ",threadCount)
