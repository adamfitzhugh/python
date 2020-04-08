#1. Using Netmiko, establish a connection to a network device and print out the device's prompt.

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

try:
    device = raw_input("Enter host: ")
except NameError:
    device = input("Enter host: ")

net_connect = Netmiko(host=device, username="cisco", password=getpass(), device_type="cisco_ios")
print(net_connect.find_prompt())
