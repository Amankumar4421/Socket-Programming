import socket
import os
from _thread import *
s = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0

s.bind((host, port))
print('Socket is listening..')
s.listen(5)
def multi_threaded_client(conn):
    conn.send(str.encode('Server is working:'))
    while True:
        data = conn.recv(2048)
        print("From client : ",data.decode('utf-8'))
        response = 'Server message : ' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(response))
    conn.close()
while True:
    Client, addr = s.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
s.close()