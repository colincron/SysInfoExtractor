import os

from getmac import get_mac_address
import platform
import datetime
import psutil
import urllib.request
import geocoder

def geolocation(public_ip):
    geocoded_ip = geocoder.ip(public_ip)
    return geocoded_ip.latlng

def get_public_ip_urllib():
    try:
        # Send request to icanhazip.com
        with urllib.request.urlopen('https://icanhazip.com') as response:
            # Read and decode the response (returns bytes, so decode to string)
            ip_address = response.read().decode('utf-8').strip()
            return ip_address
    except urllib.error.URLError as e:
        return f"Error fetching IP: {e.reason}"


def collector():
    system_type = platform.system()
    machine_type = platform.machine()
    network_name = platform.uname().node
    platform_arch = platform.architecture()
    time_now = datetime.datetime.now()
    nic_names = psutil.net_if_stats()
    public_ip = get_public_ip_urllib()
    coords = str(geolocation(public_ip)[0])+", "+ str(geolocation(public_ip)[1])
    python_version = platform.python_version()

    print("\n\nSystem Info Extractor by Colin Cron\n")
    print(time_now)
    print("\nSystem Information: \n")
    print("Operating System: " + system_type)
    print("Network Name: " + network_name)
    print("Platform Architecture: " + platform_arch[0])
    print("Machine: " + machine_type)
    print("Python version: " + python_version)

    print("\nPublic IP: " + public_ip)
    print("IP-based Geolocation Coords: " + coords)

    print("\nNetworking Interfaces: ")
    try:
        for nic_name in nic_names:
            print("\nInterface: " + nic_name + "\nMac Address: " + get_mac_address(nic_name))
            print("IPV4 address: " + psutil.net_if_addrs()[nic_name][0][1])
            print("Subnet mask: " + psutil.net_if_addrs()[nic_name][0][2])

    except TypeError:
        print("\nInterface: " + nic_name + "\nMac Address: None")
        print("IPV4 address: " + psutil.net_if_addrs()[nic_name][0][1])
        print("Subnet mask: " + psutil.net_if_addrs()[nic_name][0][2])

