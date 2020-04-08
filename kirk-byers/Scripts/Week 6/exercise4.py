#4. Use send_config_set() and send_config_from_file() to make configuration changes.
#The configuration changes should be benign. For example, on Cisco IOS I typically change the logging buffer size.
#As part of your program verify that the configuration change occurred properly. For example, use send_command() to execute 'show run' and verify the new configuration.

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

def printer(output):
    print()
    print('-' * 80)
    print(output)
    print('-' * 80)
    print()

try:
    device = raw_input("Enter host: ")
except NameError:
    device = input("Enter host: ")

password = getpass()

iol1 = {
host=device, username="cisco", password=getpass(), device_type="cisco_ios",
}

net_connect = Netmiko(**iol1)

configuration = ["logging console", "logging buffer 10000"]
output = net_connect.send_config_set(config)
printer(output)

output = net_connect.send_config_from_file("config.txt")
printer(output)

message = "Checking config change\n"
output = net_connect.send_command("show run | inc logging")
if '8000' in output:
    message += "Buffer size is 8000"
else:
    message += "Buffer is incorrect"
printer(message)
