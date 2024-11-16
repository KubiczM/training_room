from hosts_file import add_host
from hosts_file import loaded_hosts_from_file
from scan import scan_hosts_from_file
from request import get_data_from_hosts_file


def run_program():
    add_host("forcedeye.com", "onet.pl")

    hosts = loaded_hosts_from_file()
    print(f"Loaded hosts: {hosts}")

    scan_hosts_from_file()

    get_data_from_hosts_file()


if __name__ == "__main__":
    run_program()
