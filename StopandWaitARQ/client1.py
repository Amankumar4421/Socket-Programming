import socket
c1 = socket.socket()
host = '127.0.0.1'
port = 2004
print('Waiting for connection response')
c1.connect((host, port))
res = c1.recv(1024)
while True:
    Input = input('Enter to send : ')
    if Input == 'exit':
        break
    c1.send(str.encode(Input))
    res = c1.recv(1024)
    print(res.decode('utf-8'))
c1.close()