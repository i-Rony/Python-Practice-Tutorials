from socket import *

server_addr = ('192.168.230.1', 9999)

s = socket(AF_INET, SOCK_DGRAM)
s.bind(server_addr)

while True:
    data,addr = s.recvfrom(1024)
    print(data.decode('ascii'))
    msg = "This is from the server"
    s.sendto(msg.encode('ascii'),addr)