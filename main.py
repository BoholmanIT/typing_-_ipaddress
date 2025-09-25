import typing
import ipaddress

"""Задание: Написать функцию с явной типизацией (typing), которая принимает список IP-адресов в виде строк и список подсетей (строка с CIDR, например "192.168.1.0/28"), а возвращает словарь, где ключ — подсеть, а значение — список IP-адресов, принадлежащих этой подсети.
Требования:
Использовать стандартный модуль ipaddress для проверки принадлежности IP к подсети.

Использовать typing для указания типов аргументов и возвращаемого значения:

IP-адреса и подсети — строки.

Результат — Dict[str, List[str]].

Функция должна корректно обрабатывать IP, которые не принадлежат ни одной из подсетей (пропускать их).

Реализовать проверку на валидность IP и подсетей, выбрасывая исключение при ошибке."""

def group_ips_by_subnet(ips: typing.List[str], networks: typing.List[str]) -> typing.Dict[str, typing.List[str]]:
    ratio: typing.Dict[str, typing.List[str]] = {}
    ip_in_network: typing.List[str] = []
    for network in networks:
        ip_in_network: typing.List[str] = []
        for ip in ips:
            try:
                if ipaddress.ip_address(ip) == ipaddress.ip_network(network):
                    ip_in_network.append(ip)
            
            except Exception as e:
                print(e)
            finally:
                pass
        ratio[network] = ip_in_network.copy()
    
    return ratio.copy()


if __name__ == "__main__":
    
    ips = ["127.120.1.251", "127.120.1.99", "127.120.1.242", "192.168.0.1"]
    subnets = ["127.120.1.96/28", "127.120.1.240/28"]

    result = group_ips_by_subnet(ips, subnets)
    print(result)