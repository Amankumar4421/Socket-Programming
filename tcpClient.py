import socket

c_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c_socket.connect(("localhost",9999))

while True:
    st = input("Enter to Send : ")
    c_socket.send(st.encode('utf-8'))
    # data=c_socket.recv(1024).decode('utf-8')
    ch = input("send more? (y/n) : ")
    if ch == 'y':
        continue
    else:
        break
c_socket.close()
