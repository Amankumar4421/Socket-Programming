#This is for clint
import socket
c = socket.socket()
r = input("Enter the extension of your received file - jpg , png , bmp , mp4 : ")
s = "received." + r
print(s)
condition = True
c.connect(('localhost',4421))
f = open(s,"wb")
while condition:
    image = c.recv(1024)
    if str(image) == "b''":
        condition = False
    f.write(image)