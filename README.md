# IP Range Port Scanner

This Python script allows you to scan a given IP range to check if a specific port (e.g., port 8443) is open for each IP. It then saves the IP addresses with an open port to a CSV file.

## How it works

The script uses the `socket` library to establish a TCP connection to each IP address in the specified range on the specified port. If the connection is successful, it means the port is open, and the IP address is recorded in the CSV file.

## Prerequisites

- Python 3.x

## How to use

1. Clone the repository to your local machine:git clone https://github.com/rick001/ip-scanner.git
   
2. Navigate to the project directory: cd ip-range-port-scanner

3. Execute the Python script: python ip_scanner.py

4. When prompted, enter the IP range you want to scan in CIDR notation (e.g., 1.2.0.0/24).

5. The script will scan all the IP addresses in the range for port 8443. If an IP address has the port open, it will be displayed on the screen.

6. The results will be saved in a CSV file named `open_ports.csv` in the same directory.

**Note:** Ensure you have the necessary permissions and authorization to perform network scanning. Unauthorized scanning can have serious legal consequences.

