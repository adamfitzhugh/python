#3. Find a command on your device that has additional prompting. Use send_command_timing to send the command down the SSH channel. Capture the output and handle the additional prompting.

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

file = 'thisfile.txt'
command = "delete flash:{}".format(file)
net_connect = Netmiko(**iol1)
output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)
if 'confirm' in output:
    output += net_connect.send_command_timing('n', strip_prompt=False, strip_command=False)
else:
    raise ValueError("Confirm message in output")

print()
print('-' * 80)
print(output)
print('-' * 80)
print()
