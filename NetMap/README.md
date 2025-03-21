# 🔎 NetMap — Local Network Scanner

NetMap is a Python-based tool that uses ARP and Nmap to discover devices on your local network. It identifies IP addresses, MAC addresses, hostnames, and open services — making it great for network diagnostics, recon, or teaching yourself how networks behave.

---

## 🚀 Features

- Fast ARP scan to find live devices
- Displays MAC & IP addresses
- Uses Nmap to:
  - Resolve hostnames
  - Identify open ports
  - Fingerprint running services
- Clean, readable output for terminal use

---


## 📦 Requirements

Install dependencies with pip, and ensure Nmap is installed and available in your system `PATH`.

```bash
pip install scapy psutil python-nmap
