#5. Optional, use send_command() in conjunction with ntc-templates to execute a show command. Have TextFSM automatically convert this show command output to structured data.

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

try:
    device = raw_input("Enter host: ")
except NameError:
    device = input("Enter host: ")

password = getpass()

iol1 = {
host=device, username="cisco", password=getpass(), device_type="cisco_ios",
}

command = "show int status"
net_connect = Netmiko(**iol)
output = net_connect.send_command(command, use_textfsm=True)
print()
print('-' * 80)
pprint(output)
print('-' * 80)
print()
