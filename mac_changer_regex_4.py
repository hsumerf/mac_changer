#!/usr/binenv python

import subprocess
from optparse import OptionParser
import re

def get_arguments():

    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    # key-value pairs, arguments and their values coming
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Plese specify an interface, use --help for more info.")
    if not options.new_mac:
        parser.error("[-] Plese specify mac address, use --help for more info.")
    return options

def change_mac(interface,new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig",interface, "down"])
    subprocess.call(["ifconfig", interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    mac_address_search_result = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    if mac_address_search_result:
        print(mac_address_search_result.group(0))
    else:
        print("Could not Read MAC address")
options = get_arguments()
change_mac(options.interface,options.new_mac)

get_current_mac(options.interface)