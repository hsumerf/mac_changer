#!/usr/binenv python

import subprocess
import optparse


parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
(options,arguments) = parser.parse_args()
if not options.interface:
    parser.error("[-] Plese specify an interface, use --help for more info.")
if not options.new_mac:
    parser.error("[-] Plese specify mac address, use --help for more info.")

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig",interface, "down"])
subprocess.call(["ifconfig", interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])
