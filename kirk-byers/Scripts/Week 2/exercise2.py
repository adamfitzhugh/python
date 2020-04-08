"""Create a list of five IP addresses.
Use the .append() method to add an IP address onto the end of the list. Use the .extend()
method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.
Print out the entire list of ip addresses. Print out the first IP address in the list. Print out
the last IP address in the list.
Using the .pop() method to remove the first IP address in the list and the last IP address in
the list.
Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address
in the list.
"""

from __future__ import print_function, unicode_literal

ip_addr_list = ["192.168.1.1", "172.16.1.1", "8.8.8.8", "4.4.4.4", "10.1.1.1"]
ip_addr_list.append("205.169.25.4")
ip_addr_list.extend(["1.1.1.1", "2.2.2.2"])
ip_addr_list = ip_addr_list + ["20.20.20.20", "30.30.30.30"]
print(ip_addr_list)
print(ip_addr_list[0])
print(ip_addr_list[-1])

first_ip = ip_addr_list.pop(0)
last_ip = ip_addr_list.pop()

ip_addr_list[0] = "3.3.3.3"
print(ip_addr_list[0])
