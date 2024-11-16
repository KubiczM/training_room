import subprocess
from hosts_file import loaded_hosts_from_file

def host_scan(host): # skanuje hosta
    print(f"\nStarting host scanning: {host}")
    try:
        result = subprocess.run(
            ['nmap', '-sS', '1-65535', host],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"Scan result for {host}:\n{result.stdout}")
            return result.stdout
        else:
            print(f"Error while scanning {host}: {result.stderr}")
            return None
    except FileNotFoundError:
        print("'nmap' was not found. Make Sure it its installed")
        return None


def scan_hosts_from_file(file="hosts.txt"): # wczytuje hosty z pliku i skanuje je host_scan'em
    hosts_from_file = loaded_hosts_from_file(file)

    if hosts_from_file:
        for host in hosts_from_file:
            host_scan(host)
    else:
        print("No hosts to scan.")



