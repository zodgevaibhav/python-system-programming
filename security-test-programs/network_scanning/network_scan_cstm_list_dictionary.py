#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # set destination ip or ip range
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # set desetination mac as broadcast mac
    arp_request_broadcast = broadcast/arp_request
    answers, unanswered = scapy.srp(arp_request_broadcast,timeout=1, verbose=False)
    print("--------------------------------------------------------------------")
    print("  IP  \t\t\t\t MAC  ")
    print("--------------------------------------------------------------------")

    machine_list=[]
    for element in answers:
        #print(element[0].show())
        #print(element[1].show())
        machine_list.append({"ip": element[1].psrc, "mac": element[1].hwsrc})
        print(element[1].psrc+"\t\t\t"+element[1].hwsrc)


    #print(arp_request.summary())
    #print(broadcast.summary())
    #print(arp_request_broadcast.show())
    #scapy.ls(scapy.ARP())
    #scapy.ls(scapy.Ether())

    print("\n\n------------------- Dictionary Print -----------------------------------\n")

    print(machine_list[0].get("ip")+" - "+machine_list[0].get("mac"))
    print(machine_list[1].get("ip")+" - "+machine_list[1].get("mac"))
    print(machine_list[2].get("ip")+" - "+machine_list[2].get("mac"))

scan("10.0.2.1/24")
