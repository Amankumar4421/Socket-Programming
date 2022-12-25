#client
import socket
c_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    domain = input("Enter Domain Name : ")
    reply = c_socket.sendto(domain.encode('utf-8'),('localhost',4421))
    data, addr = c_socket.recvfrom(1024)
    print("The Ip Address is : ",data.decode('utf-8'))
    if input("Continue?(y/n)")=='n':
        break
c_socket.close()