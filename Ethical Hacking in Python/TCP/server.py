from socket import *

host = "192.168.230.1"
port = 9999

s = socket(AF_INET,SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
    c,addr = s.accept()
    print("[+] Got connection from ", addr)
    R_msg = s.recv(1024)
    print(R_msg.decode('ascii'))
    msg = "This is from server"
    c.send(msg.encode('ascii'))
    c.close() 