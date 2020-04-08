"""
Create a dictionary representing a network device. The dictionary should have key-value pairs
representing the 'ip_addr', 'vendor', 'username', and 'password' fields.
Print out the 'ip_addr' key from the dictionary.
If the 'vendor' field is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' field is
'juniper', then set the 'platform' to 'junos'.
Create a second dictionary named bgp_fields. The bgp_fields should have a key for 'bgp_as',
'peer_as', and 'peer_ip'.
Using the .update() method add the bgp_fields key-value pairs to the network device dictionary.
Using a for-loop iterate over the dictionary and print out all of the dictionary keys.
Using a single for-loop iterate over the dictionary and print out all of the dictionary keys and
values.
"""

from __future__ import print_function, unicode_literals


devices = {
    'ip': '10.10.10.10',
    'vendor': 'cisco',
    'username': 'cisco',
    'password': 'cisco',
}


print()
print(devices['ip'])
print()


if devices['vendor'].lower() == 'cisco':
    devices['platform'] = 'ios'
elif devices['vendor'].lower() == 'juniper'
    devices['platform'] = 'junos'


bgp = {
    'as': 42,
    'peer': 100,
    'peer_ip': '172.16.1.1'
}


devices.update(bgp)

print('-' * 80)
for key in devices:
    print("{:>15}".format(key))
print('-' * 80)
print()


print('-' * 80)
for key, val in devices.items():
    print("{key:>15} ---> {val:>15}".format(key=key, value=val))
print('-' * 80)
print()
