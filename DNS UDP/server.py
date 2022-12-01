#server
import socket
table = {'www.google.com':'192.165.1.1','www.youtube.com':'192.165.1.2','www.facebook.com':'192.165.1.3','www.twitter.com':'192.165.1.4'}

s_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_socket.bind(('localhost',4421))
print("Server Waiting...")
while True:
    data , addr = s_socket.recvfrom(1024)
    print("Conected with : ",addr)
    data = data.decode()
    ip = table.get(data,"Not Found!").encode()
    send = s_socket.sendto(ip,addr)