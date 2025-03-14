#!/usr/bin/env python

import subprocess  # run command
import optparse  # parse commandline argument


def parse_arguments():

    parser = optparse.OptionParser()  # Object creation of OptionParser class

    parser.add_option("-i", "--interface", dest="interface", help="Provide interface ti change its MAC address")
    parser.add_option("-m", "--mac", dest="macChangeTo", help="Provide MAC to change to")

    (options, arguments) = parser.parse_args()  # arguments will be stored to arguments variable, options store to
    if not options.interface:
        parser.error(" Please specify interface")
    elif not options.macChangeTo:
        parser.error(" Please specify mac adress to change")
    else:
        # option variable
        return options


def change_mac(interface, mac_change_to):
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether "+mac_change_to, shell=True)
    # subprocess.call("ifconfig " + interface + " up",shell=True)
    subprocess.call(["ifconfig", interface, "up"])  # secure version of the function as command injection will be
    # avoided
    return "Successfully changed mac address"


options = parse_arguments()
print(change_mac(options.interface, options.macChangeTo))
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
