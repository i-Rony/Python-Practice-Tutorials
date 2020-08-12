from socket import *

server_addr = ('192.168.230.1', 9999)

s = socket(AF_INET, SOCK_DGRAM)

msg = "THIS IS FROM THE CLIENT"
s.sendto(msg.encode('ascii'),server_addr)

data,server = s.recvfrom(1024)
print(data.decode('ascii'))