import socket
c2 = socket.socket()
host = '127.0.0.1'
port = 2004
print('Waiting for connection response')
c2.connect((host, port))
res = c2.recv(1024)
while True:
    Input = input('Enter to send : ')
    if Input == 'exit':
        break
    c2.send(str.encode(Input))
    res = c2.recv(1024)
    print(res.decode('utf-8'))
c2.close()