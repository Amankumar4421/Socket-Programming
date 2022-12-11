#This is for socket
import socket
c = 0
s = socket.socket()
s.bind(('localhost',4421))
path = input("Enter full Path: ")
path = str(path)
image = open(path,"rb")
s.listen(1)
c,address = s.accept()
if c != 0:
    for i in image:
        c.send(i)