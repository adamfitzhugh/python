from __future__ import print_function, unicode_literals

'Create a script which declares the below variables and prints out the below. f is the format which formats the print and gives each line 20 and 8 spaces'

ip_addr1 = '192.168.1.1'
port1 = 80
ip_addr2 = '192.168.2.1'
port2 = 443


print(f"My IP Address is: {ip_addr1:^20} {port1:^8}")
print(f"My IP Address is: {ip_addr2:^20} {port2:^8}")

