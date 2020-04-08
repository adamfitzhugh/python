"""
Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with
a default value of 'cisco_ios'. Print all four of the function variables out as part of the
function's execution.
Call the 'ssh_conn2' function both with and without specifying the device_type
Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using
the **kwargs technique.
"""

from __future__ import print_function, unicode_literals

def ssh_conn(ip_addr, username, password, device_type):
    print("The IP address is: {}".format(ip_addr))
    print("The username is: {}".format(username))
    print("The password is: {}".format(password))
    print("The device type is: {}".format(device_type))

#Positional args without device_type
ssh_conn = ('10.1.1.1', 'admin', 'cisco')

##Positional args with device_type
ssh_conn2 = ('10.1.1.1', 'admin', 'cisco', 'cisco_ios')

#Named args
named_args = (ip_addr='10.1.1.1', username='admin', password='cisco')

#Mix of positional and named args
mixed_args = (ip_addr='10.1.1.1', username='admin', password='cisco')

#Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the **kwargs technique
dict = {"ip_addr": "10.1.1.1",
        "username": "admin",
        "password": "cisco",
        "device_type": "cisco_ios"}

ssh_conn2(**dict)
