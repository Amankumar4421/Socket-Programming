import socket

s_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_socket.bind(("localhost",9999))

while True:
    data, addr = s_socket.recvfrom(4096)
    print(data.decode('utf-8'))
    st = input("Enter Reply : ")
    s_socket.sendto(st.encode('utf-8'),addr)