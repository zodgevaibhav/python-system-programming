#!/usr/bin/env python

import subprocess  # run command
import optparse  # parse commandline argument

parser = optparse.OptionParser()  # Object creation of OptionParser class

parser.add_option("-i", "--interface", dest="interface", help="Provide interface ti change its MAC address")
parser.add_option("-m", "--mac", dest="macChangeTo", help="Provide MAC to change to")

(options, arguments) = parser.parse_args()  # arguments will be stored to arguments variable, options store to option
# variable
macChangeTo = options.macChangeTo
interface = options.interface

# interface = input("Enter Interface > ")  # python 3 function, we need to run the script by python3 scriptname
# macChangeTo = input("Enter new mac address > ")

subprocess.call("ifconfig " + interface + " down",shell=True)
subprocess.call("ifconfig " + interface + " hw ether "+macChangeTo, shell=True)
# subprocess.call("ifconfig " + interface + " up",shell=True)
subprocess.call(["ifconfig", interface, "up"])  # secure version of the function as command injection will be avoided
