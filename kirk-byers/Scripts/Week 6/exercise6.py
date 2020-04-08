#6. Optional, connect to three networking devices one after the other. Use send_command() to execute a show command on each of these devices. Print this output to the screen.

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

try:
    device = raw_input("Enter host: ")
except NameError:
    device = input("Enter host: ")

password = getpass()

iol1 = {
'host':"device", 'username':"cisco", 'password':"password", 'device_type':"cisco_ios", 'command': "show interfaces"
}
iol2 = {
'host':"device", 'username':"cisco", 'password':"password", 'device_type':"arista_eos", 'command': "show interfaces"
}
iol3 = {
'host':"device", 'username':"cisco", 'password':"password", 'device_type':"cisco_nxos", 'command': "show interfaces"
}

for device in (iol1, iol2, iol3):
    command = device.pop('command')
    net_connect = Netmiko(**device)
    output = net_connect.send_command(command)
    print()
    print('-' * 80)
    print("{}: {}".format(device['host'], device['device_type']))
    print(output)
    print('-' * 80)
    print()
