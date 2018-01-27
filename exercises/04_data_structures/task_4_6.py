# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split()
ospf_route[0] = 'OSPF'
ospf_route_template = '''               
Protocol:\t\t{}
Prefix:\t\t\t{}
AD/Metric:\t\t{}
Next-Hop:\t\t{}
Last update:\t\t{}
Outbound Interface:\t{}
'''
print(ospf_route_template.format(ospf_route[0], ospf_route[1], ospf_route[2], ospf_route[4], ospf_route[5], ospf_route[6]))

