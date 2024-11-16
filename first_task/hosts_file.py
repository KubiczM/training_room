hosts = []


def add_host(*args,):  # dodaje hosty do listy 'hosts' i zapisuje je w pliku, unikając duplikatów
    current_hosts = loaded_hosts_from_file()

    for host in args:
        if host not in current_hosts and host not in hosts:
            hosts.append(host)
        else:
            print(f"\nHost '{host}' already exists in list.")

    print("\nHosts added:")
    for host in args:
        print(host)

    save_hosts(args)


def save_hosts(new_hosts):  # tutaj jest tworzenie wyzej wspomnianego pliku
    current_hosts = loaded_hosts_from_file()

    with open("hosts.txt", "a") as file:
        for host in new_hosts:
            if host not in current_hosts:
                file.write(f"{host}\n")
            else:
                print(f"\nHost '{host}' already exists in the file.")

    print("\nList of hosts saved in file 'hosts.txt'.")


def loaded_hosts_from_file(text_file="hosts.txt"):  # wczytuje hosty z hosts.txt
    try:
        with open(text_file, "r") as file:
            loaded_hosts = [line.strip() for line in file if line.strip()]  # usuwam puste linie
        return loaded_hosts
    except FileNotFoundError:
        print(f"File '{text_file}' not found.")
        return []