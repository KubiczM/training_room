# use subprocess to pull the data by nmap from https://www.forcedeye.com
import subprocess


def get_SYN_scan(host):
    result = subprocess.run(["nmap", "-sS", host], capture_output=True, text=True)
    print(result.stdout)
    print(result.stdout)


def get_UDP_scan(host):
    result = subprocess.run(["nmap", "-sU", "-Pn", host], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)


host = "forcedeye.com"


if __name__ == "__main__":
    get_SYN_scan(host)
    get_UDP_scan(host)
