#Exercises
#Reference code for these exercises is posted on GitHub at:
#https://github.com/ktbyers/pynet/tree/master/learning_python/lesson1

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#1 - Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3 (representing three corresponding IP addresses). Print these three variables to standard output using a single print statement.
#a - Make your print statement compatible with both Python2 and Python3.
#b - If you are using either Linux or MacOS make your program executable by adding a shebang line and by changing the files permissions (i.e. chmod 755 exercise1.py).


#!/usr/bin/python
from __future__ import print_function

ip_addr1 = 192.168.1.1
ip_addr2 = 10.10.10.1
ip_addr3 = 172.16.1.1

print(ip_addr1, ip_addr2, ip_addr3)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#2 - Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.
#a - Your program output should look like the following:
​ #$ python exercise2.py
#Please enter an IP address: 80.98.100.240

    #Octet1         Octet2         Octet3         Octet4
#------------------------------------------------------------
      #80             98             100            240
   #0b1010000      0b1100010      0b1100100     0b11110000
     #0x50           0x62           0x64           0xf0
#------------------------------------------------------------

#Four columns, fifteen characters wide, a header column, data centered in the column.

from __future__ import print_function

try:
    ip_addr = raw_input("Please enter an IP address:")
except NameError:
    ip_addr = input("Please enter an IP address:")


octets = ip_addr.split(".")
print()
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(octets[0])), bin(int(octets[1])),
                                        bin(int(octets[2])), bin(int(octets[3]))))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(octets[0])), hex(int(octets[1])),
                                        hex(int(octets[2])), hex(int(octets[3]))))
print("-" * 60)
print()


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#3 - Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator. The second variable should use all upper case characters with underscore as the word separator. The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.
#a - Make all three variables be strings that refer to IPv6 addresses.
#b - Use the from future technique so that any string literals in Python2 are unicode.
#c - compare if variable1 equals variable2
#d - compare if variable1 is not equal to variable3

from __future__ import print_function

ipv_six_addr_1 = "2001:db8:1234::1"
IPV_SIX_ADDR_2 = "2001:db8:1234::2"
ipv_6_addr_3 = "2001:db8:1234::3"

print("")
print("Is var1 == var2: {}".format(ipv_six_addr_1 == IPV_SIX_ADDR_2))
print("Is var1 != var3: {}".format(ipv_six_addr_1 != ipv_6_addr_3))
print("")

-------------------------------------------------------------------------------------------------------------


#4 - Create a show_version variable that contains the following
    #show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
#a - Remove all leading and trailing whitespace from the string.
#b - Split the string and extract the model and serial_number from it.
#c - Check if 'Cisco' is contained in the model string (ignore capitalization).
#d - Check if '881' is in the model string.
#e - Print out both the serial number and the model.


from __future__ import print_function

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()

fields = show_version.split()
model = fields[1]
serial_number = fields[2]

print()

cisco_vendor = 'cisco' in model.lower()
print("Checking if Model is Cisco: ".format(cisco_vendor))

model_881 = '881' in model
print("Checking if Model contains 881: ".format(model_881))

print("Serial Number: {}".format(serial_number))
print("Model: {}".format(model))
print()

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#5 - You have the following three variables from the arp table of a router:

#mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
#mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
#mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

#Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:

#             IP ADDR          MAC ADDRESS
#-------------------- --------------------
#        10.220.88.29       5254.abbe.5b7b
#        10.220.88.30       5254.ab71.e119
#        10.220.88.32       5254.abc7.26aa

#Two columns, 20 characters wide, data right aligned, a header column.


from __future__ import print_function, unicode_literals

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"


fields = mac1.split()
ip_addr1 = fields[1]
mac1 = fields[3]

fields = mac2.split()
ip_addr2 = fields[1]
mac2 = fields[3]

fields = mac3.split()
ip_addr3 = fields[1]
mac3 = fields[3]


print()
print("{:>20} {:>20}".format("IP ADDR", "MAC ADDRESS"))
print("{:>20} {:>20}".format("-" * 20, "-" * 20))
print("{:>20} {:>20}".format(ip_addr1, mac1))
print("{:>20} {:>20}".format(ip_addr2, mac2))
print("{:>20} {:>20}".format(ip_addr3, mac3))
print()
