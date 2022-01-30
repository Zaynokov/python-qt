import ipaddress
import subprocess
from pprint import pprint
from tabulate import tabulate


def ip_address(host):
    if type(host) == int:
        return ipaddress.ip_address(host)
    elif type(host) == str:
        return host
    else:
        return False


def host_ping(lst):
    result = []
    for host in lst:
        ip = ip_address(host)
        if subprocess.call(["ping", "-n", "2", "-w", "2", ip]) == 0:
            result.append(str(ip) + ' - Узел доступен')
        else:
            result.append(str(ip) + ' - Узел недоступен')
    return result


def host_range_ping(lst):
    result = []
    for ip in lst:
        if subprocess.call(["ping", "-n", "2", "-w", "2", ip]) == 0:
            result.append(str(ip) + ' - Узел доступен')
        else:
            result.append(str(ip) + ' - Узел недоступен')
    return result


def host_range_ping_tab(lst):
    head = [('Доступные', 'Недоступные')]
    table = [[], []]
    for ip in lst:
        if subprocess.call(["ping", "-n", "2", "-w", "2", ip]) == 0:
            table[0].append(str(ip))
        else:
            table[1].append(str(ip))
    head.extend(list(zip(*table)))
    if len(table[0]) > len(table[1]):
        for item in table[0][len(table[1]):]:
            head.append((item, None))
    elif len(table[0]) < len(table[1]):
        for item in table[1][len(table[0]):]:
            head.append((None, item))
    print(tabulate(head, headers='firstrow', stralign='center',
                   tablefmt='pipe'))


# tuples_list = [['Python', 'interpreted', '1991'],
#                ['JAVA', 'compiled', '1995'],
#                ['С', 'compiled', '1972']]
# print(tabulate(tuples_list, headers=['1', '2', '3']))

if __name__ == '__main__':
    ips = ['yandex.com', 'gb.ru', '127.0.0.1', 'cb', '24452462345', 'thisnotip']
    hosts = list(map(str, ipaddress.ip_network('80.0.1.0/28').hosts()))
    # pprint(host_ping(ips))
    # pprint(host_range_ping(hosts))
    print(host_range_ping_tab(['yandex.com', 'gb.ru', '127.0.0.1', 'cb', '24452462345', 'thisnotip']))
