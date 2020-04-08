Exercises

Reference code for these exercises is posted on GitHub at:
https://github.com/ktbyers/pynet/tree/master/learning_python/lesson8



1a. Import the 'datetime' library. Print out the module that is being imported by datetime (the __file__ attribute)

Import the Python ipaddress library. Print out the module that is being imported by ipaddress (the __file__ attribute). If you are using Python 2.7, you will need to pip install the ipaddress library.

Import sys and use pprint to pprint sys.path


1b. In a separate Python file named 'my_devices.py', define a dictionary named 'rtr1' with the following key-value pairs:
host = rtr1.domain.com
username = cisco
password = cisco123
device_type = cisco_ios

Import my_devices into this program, and print the rtr1 dictionary to the screen using pprint.


1c. In a Python shell, try importing the 'my_devices' when my_devices.py is not in your current working directory.

What exception do you get when you do this?

Update your PYTHONPATH environment variable so that you are successfully able to import this module.


2a. Create a new virtual environment on your system named 'test_venv'.

b. Activate the virtual environment

c. Use 'which python' to see the path of the Python that you are using.

d. Use 'pip list' to see the packages you have installed.

e. Use pip to install Netmiko and the requests library.

f. Use 'pip list' to see the updated list of installed packages.


3a. Using the same 'test_venv' that you created in exercise2, install netmiko version 2.0.1. Verify that this version is installed by executing the following from the Python shell:
>>> import netmiko
>>> netmiko.__version__
'2.0.1'

b. Using pip, upgrade your version of Netmiko to the latest version.

c. Deactivate your virtual environment. See 'which python' is now being used.


4a. Activate your 'test_venv' virtual environment.

b. Use pip to uninstall the Netmiko library.

c. Verify that Netmiko is no longer installed.

d. Use pip to install the 'develop' branch of Netmiko.
