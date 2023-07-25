import socket
import ipaddress
import csv

def check_port_open(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout in seconds
            s.connect((ip, port))
            return True
    except socket.timeout:
        return False
    except ConnectionRefusedError:
        return False
    except OSError as e:
        if e.errno == 113:
            return False
        else:
            raise

def scan_ip_range(ip_range, port):
    open_ports = []
    unreachable_ips = []

    # Parse the IP range
    network = ipaddress.ip_network(ip_range, strict=False)

    # Iterate through each IP address in the range
    for ip in network:
        ip_str = str(ip)
        if check_port_open(ip_str, port):
            open_ports.append(ip_str)
        else:
            unreachable_ips.append(ip_str)

    return open_ports, unreachable_ips

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['IP Address'])
        writer.writerows([[ip] for ip in data])

if __name__ == "__main__":
    ip_range = input("Enter IP range (e.g., 1.2.0.0/24): ")
    port = 8443
    output_file = "open_ports.csv"

    open_ports, unreachable_ips = scan_ip_range(ip_range, port)

    if open_ports:
        print("The following IP addresses have port 8443 open:")
        for ip in open_ports:
            print(ip)

        write_to_csv(output_file, open_ports)
        print(f"Results saved to {output_file}")
    else:
        print("No IP address with port 8443 open.")

    if unreachable_ips:
        print("The following IP addresses are unreachable:")
        for ip in unreachable_ips:
            print(ip)

