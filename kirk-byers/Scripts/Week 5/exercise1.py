"""
Create an ssh_conn function. This function should have three parameters: ip_addr, username, and
password. The function should print out each of these three variables and clearly indicate which
variable it is printing out.
Call this ssh_conn function using entirely positional arguments.
Call this ssh_conn function using entirely named arguments.
Call this ssh_conn function using a mix of positional and named arguments.
"""

from __future__ import print_function, unicode_literals

def ssh_conn(ip_addr, username, password):
    print("The IP address is: {}".format(ip_addr))
    print("The username is: {}".format(username))
    print("The password is: {}".format(password))

#Positional args
ssh_conn = ('10.1.1.1', 'admin', 'cisco')

#Named args
named_args = (ip_addr='10.1.1.1', username='admin', password='cisco')

#Mix of positional and named args
mixed_args = (ip_addr='10.1.1.1', username='admin', password='cisco')
