import socket
from datetime import datetime

HOST = "192.168.43.49"
PORT = 8484
max_size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

print('Starting Server at: ', datetime.now())
print('Waiting for Incoming Connection from Client ...')

sock.listen(5)
client, addr = sock.accept()

while True:
    data = client.recv(max_size)
    if data.decode('utf-8') == 'q':
        break
    print("At ", datetime.now(), addr, " said ", data.decode('utf-8'))
    mtc = input("Enter Message: ")
    mtc_encoded = mtc.encode('utf-8')
    client.send(mtc_encoded)
    if mtc == 'q':
        break

client.close()
sock.close()