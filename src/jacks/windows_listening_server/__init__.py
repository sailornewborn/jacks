import psutil
from socket import AF_INET


def get_LAN_ip_windows() -> str:
    possible_ip = None
    all_interfaces = psutil.net_if_addrs()
    for name, infos in all_interfaces.items():
        for set in infos:
            if set.address.startswith("192.") and set.family == AF_INET:
                possible_ip = set.address
    return possible_ip