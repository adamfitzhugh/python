#Exercises
#Reference code for these exercises is posted on GitHub at:
#https://github.com/ktbyers/pynet/tree/master/learning_python/lesson2



#1 - Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file contents to a variable. Print out the file contents to the screen. Also print out the type of the variable (you should have a string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement). Read in the file contents using the .readlines() method. Print out the file contents to the screen. Also print out the type of the variable (you should have a list at this point).


from __future__ import print_function, unicode_literals

f = open("show_version.txt")

show_version = f.read()
print(show_version)
print(type(show_version))
f.close()

with open("show_version.txt") as f:
    show_ver = f.readlines()

print(show_version)
print(type(show_version))

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.


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




3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:
from pprint import pprint
pprint(some_var)

Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".

from __future__ import print_function, unicode_literals
from pprint import pprint

with open("show_arp.txt") as f:
    show_arp = f.readlines()

show_arp = show_arp[1:]
pprint(show_arp)

show_arp.sort()
entries = show_arp[:3]
entries = '\n'.join(entries)

with open("arp_entries.txt", "wt") as f:
    f.write(entries)



4. Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.

Obtain the list entry associated with the FastEthernet4 interface. You can just hard-code the index at this point since we haven't covered for-loops or regular expressions. Use the string .split() method to obtain both the IP address and the corresponding interface associated with the IP.

Create a two element tuple from the result (intf_name, ip_address).

Print that tuple to the screen.

Use pycodestyle on this script. Get the warnings/errors to zero. You might need to 'pip install pycodestyle' on your computer (you should be able to type this from the shell prompt). Alternatively, you can type 'python -m pip install pycodestyle'.


from __future__ import print_function, unicode_literals

with open("show_ip_int_brief.txt") as f:
    show_ip_int_brief = f.readlines()

fa4_ip = show_ip_int_brief[5].strip()
fields = fa4_ip.split()
int = fields[0]
ip_addr = fields[1]

results = (int, ip_addr)
print(results)


5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.


from __future__ import print_function, unicode_literals

with open("show_ip_bgp_summ.txt") as f:
    show_ip_bgp_summ = f.readlines()


bgp_summ = bgp_summ.splitlines()

first_line = bgp_summ[0]
as_num = first_line.split()[-1]
print("Local AS Number: {}".format(as_num))

last_line = bgp_summ[-1]
peer = last_line.split()[0]
print("BGP Peer IP: {}".format(peer))
