import time
import requests
from hosts_file import loaded_hosts_from_file

def add_www_to_domain(domain): # dodaje www. do domeny / namp nie wymaga www. ale GET tak
    if not domain.startswith("www."):
        domain = "www." + domain
    return domain

def get_data_from_url(url, timeout=5): # zgodnie z zaleceniem timeout na 5s
    try:
        response = requests.get(url, timeout=timeout)

        if response.status_code == 200:
            print(f"Response received successfully from {url}:")
            print(response.text)
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
    except requests.exceptions.Timeout:
        print(f"Request to {url} timed out after {timeout} seconds.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while loading {url}: {e}")

def get_data_from_hosts_file(file="hosts.txt"):
    hosts = loaded_hosts_from_file(file)

    if not hosts:
        print("No hosts found in file.")
        return

    ports_to_check = range(1, 65536)

    for host in hosts:
        url_with_www = add_www_to_domain(host)
        for port in ports_to_check:
            url = f"http://{url_with_www}:{port}"
            print(f"Sending GET request to {url}")
            get_data_from_url(url)
            time.sleep(1) # opoznienie miedzy zapytaniami

