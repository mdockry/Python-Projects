#!/usr/bin/env python3
# A Basic ARP Scanner with Nmap Fingerprinting

from scapy.all import *
import ipaddress
import socket
import psutil
import nmap

nm = nmap.PortScanner()

def get_network_range():
    print("[+] Getting network range")
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect(('8.8.8.8', 80))
    ip_address = client.getsockname()[0]
    client.close()

    for iface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == socket.AF_INET and snic.address == ip_address:
                netmask = snic.netmask
                network = ipaddress.IPv4Network(f"{ip_address}/{netmask}", strict=False)
                print(f"[+] Network range: {network}")
                return network

def create_arp_packet(network):
    print("[+] Creating ARP packet")
    ip_list = [str(ip) for ip in network.hosts()]
    arp_packet = ARP(pdst=ip_list)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_packet = broadcast / arp_packet

    print("[+] Sending ARP packet...")
    ans, unas = srp(arp_request_packet, timeout=2, verbose=False)

    print(f"[+] Received {len(ans)} ARP responses.\n")

    for sent, received in ans:
        ip = received.psrc
        mac = received.hwsrc

        nm.scan(ip, arguments='-sP')
        hostname = nm[ip].hostname() if ip in nm.all_hosts() else "N/A"

        nm.scan(ip, arguments='-sV --top-ports 10')

        print("=" * 50)
        print(f"[+] IP Address   : {ip}")
        print(f"[+] MAC Address  : {mac}")
        print(f"[+] Hostname     : {hostname}")

        if 'tcp' in nm[ip]:
            print("    Open Ports:")
            for port, details in nm[ip]['tcp'].items():
                if details['state'] == 'open':
                    name = details['name']
                    product = details['product']
                    version = details['version']
                    banner = f"{product} {version}".strip()
                    print(f"      - Port {port}: {name} ({banner})")
        print("=" * 50 + "\n")

def main():
    network = get_network_range()
    create_arp_packet(network)

if __name__ == "__main__":
    main()
