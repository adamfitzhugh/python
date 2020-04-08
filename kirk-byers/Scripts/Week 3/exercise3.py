'''
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the
lines until you have encountered the remote "System Name" and remote "Port id". Save these two items
into variables and print them to the screen. You should extract only the system name and port id
from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your
loop once you have retrieved these two items.
'''

from __future__ import print_function, unicode_literals

with open("show_lldp_neighbours_detail.txt") as f:
    show_lldp = f.read()

system, port = (None, None)
for line in show_lldp.splitlines():
    if 'System Name: ' in line:
        _, system = line.split('System Name: ')
    elif 'Port ID' in line:
        _, port = line.split('Port ID: ')

    if port and system:
        break

print()
print('System Name: {}'.format(system))
print('Port ID: {}'.format(port))
print()
