"""
Using Jinja2 templating and a for-loop inside the template, generate the following configuration
snippet:
vlan 501
   name blue501
vlan 502
   name blue502
vlan 503
   name blue503
vlan 504
   name blue504
vlan 505
   name blue505
vlan 506
   name blue506
vlan 507
   name blue507
vlan 508
   name blue508
Your template should be inside your Python program for simplicity.
It is fine for your VLAN IDs to be out of order in the generated configuration (for example, VLAN
ID 508 can come before VLAN ID 504).
"""

from future import print_function, unicode_literals
import Jinja2

vlans = {
    '502': 'blue501',
    '502': 'blue502',
    '503': 'blue503',
    '504': 'blue504',
    '505': 'blue505',
    '506': 'blue506',
    '507': 'blue507',
    '508': 'blue508',
}

template = {'500_vlans': vlans}

vlan_tem = '''
{%- for vlan_id, vlan_name in vlans.items() %}
vlan {{ vlan_id }}
    name {{ vlan_name }}
{%- endfor %}

jinja_template = jinja2.Template(vlan_tem)
print(jinja_template.render(template))
