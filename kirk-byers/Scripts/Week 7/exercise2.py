"""
Using Python and Jinja2 templating generate the following OSPF configuration:
----
interface vlan 1
   ip ospf priority 100
router ospf 10
   passive-interface default
   no passive-interface Vlan1
   no passive-interface Vlan2
   network 10.10.10.0/24 area 0.0.0.0
   network 10.10.20.0/24 area 0.0.0.0
   network 10.10.30.0/24 area 0.0.0.0
   max-lsa 12000
----
The following items should be variables in your Jinja2 template:
----
ospf_process_id
ospf_priority
ospf_active_interfaces (i.e. the non-passive interfaces)
ospf_area0_networks (the three networks that are specified as belonging to area0)
----
Your template should be in an external file.
Your template should also use a conditional to control whether this is output or not:
----
interface vlan 1
   ip ospf priority 100
----
If the 'ospf_priority variable is defined', then include that section. If 'ospf_priority' is not
defined then only include the 'router ospf 10' section.
"""

from future import print_function, unicode_literals
import Jinja2

file = 'ospf_config.j2'
with open(file) as f:
    jinja_template = f.read()

ospf_int = ['Vlan1', 'Vlan2']
networks = [
    '1.1.1.0/24',
    '1.1.2.0/24',
    '1.1.3.0/24',
]

template = {
    'process_id': 10,
    'priority': 100,
    'active_interfaces': ospf_int
    'ospf_networks': networks,
}

j2_template = jinja2.Template(jinja_template)
print(template.render(template))
