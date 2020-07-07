import socket
from datetime import datetime

HOST = "192.168.43.49"
PORT = 8484
max_size = 1024

print("Starting the Client at: ", datetime.now())
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    mts = input("Enter Message: ")
    mts_encoded = mts.encode('utf-8')
    sock.send(mts_encoded)
    if mts == 'q':
        break
    data = sock.recv(max_size)
    if data.decode('utf-8') == 'q':
        break
    print("At ", datetime.now(),  " server said ", data.decode('utf-8'))

sock.close()