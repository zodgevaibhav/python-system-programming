#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # set destination ip or ip range
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # set desetination mac as broadcast mac
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast,timeout=1)
    print(answered.summary())
    print(unanswered.summary())

    #print(arp_request.summary())
    #print(broadcast.summary())
    #print(arp_request_broadcast.show())
    #scapy.ls(scapy.ARP())
    #scapy.ls(scapy.Ether())


scan("10.0.2.1/24")
