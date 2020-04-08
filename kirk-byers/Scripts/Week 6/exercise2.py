#2. Use send_command() to send a show command down the SSH channel. Retrieve the results and print the results to the screen.

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

try:
    device = raw_input("Enter host: ")
except NameError:
    device = input("Enter host: ")

iol1 = {
host=device, username="cisco", password=getpass(), device_type="cisco_ios",
}

command = "show version"
net_connect = Netmiko(**iol1)
output = net_connect.send_command(command)
print()
print('-' * 80)
print(output)
print('-' * 80)
print()
