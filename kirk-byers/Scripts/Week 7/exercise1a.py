#1a. Use Jinja2 templating to render the following:
#vlan
#   name

#Your template should be inside of your Python program for simplicity.

#The output from processing your template should be as follows. This should be printed to stdout.
#vlan 400
#   name red400

from future import print_function, unicode_literals
import Jinja2

vars = {
    'vlan_id': 400,
    'vlan_name': 'red400',
}

template = '''
vlan {{ vlan_id }}
    name {{ vlan_name }}
'''

jinja_template = jinja2.Template(template)
print(jinja_template.render(template))
