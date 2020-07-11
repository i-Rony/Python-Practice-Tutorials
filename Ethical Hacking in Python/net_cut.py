# Create iptables using the following cmd in the terminal before running the code
#
# iptables -I FORWARD -j NFQUEUE --queue-num 0

import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.drop()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

# After terminating the program
#
# iptables --flush