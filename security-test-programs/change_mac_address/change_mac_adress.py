#!/usr/bin/env python

import subprocess

interface = input("Enter Interface > ")  # python 3 function, we need to run the script by python3 scriptname
macChangeTo = input("Enter new mac address > ")

subprocess.call("ifconfig " + interface + " down",shell=True)
subprocess.call("ifconfig " + interface + " hw ether "+macChangeTo, shell=True)
# subprocess.call("ifconfig " + interface + " up",shell=True)
subprocess.call(["ifconfig", interface, "up"])  # secure version of the function as command injection will be avoided
