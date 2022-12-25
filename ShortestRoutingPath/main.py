# Driver Code for implementing Dijkstra's algorithm
import socket
import sys
import pickle

S = set()
G = []

for i in range(4):
    listo = [0, 0, 0, 0]

    for j in range(4):
        listo[j] = int(input("give input"))
    G.append(listo)

source = int(input("give source"))
destination = int(input("give destination"))
Q = []

for i in range(4):
    Q.append(i)

d = [0, 0, 0, 0]
pi = [0, 0, 0, 0]

for i in range(4):
    if i == source:
        d[i] = 0
    else:
        d[i] = 999
for i in range(4):
    pi[i] = 9000
S.add(source)
while (len(Q) != 0):

    x = min(d[q] for q in Q)
    u = 0
    for q in Q:
        if (d[q] == x):
            u = q

    print(u, "Is the minimum distance")
    Q.remove(u)
    S.add(u)
    adj = []
    for y in range(4):
        if y != u and G[u][y] != 999:
            adj.append(y)

    for v in adj:
        if d[v] > (d[u] + G[u][v]):
            d[v] = d[u] + G[u][v]
            pi[v] = u
route = []
x = destination

if pi[x] == 9000:
    print(source)
else:
    while pi[x] != 9000:
        route.append(x)
        x = pi[x]
    route.reverse()

print(route)
print(pi)
print(d)

sendingroute = pickle.dumps(route)
sockets = [8886, 8877, 8888, 8889]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), sockets))

try:
    sock.send(sendingroute)
finally:
    print("")
sock.close()
