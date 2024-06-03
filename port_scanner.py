import socket

def port_scanner(host, ports):
    """
    Scans for open ports on the target host and prints whether each port is open or closed.

    Args:
    - host: IP of the target host.
    - ports: Port numbers list to scan.

    Returns:
    - None
    """
    for port in ports:
        try:
            # Create a TCP socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Set a timeout for the connection attempt

            # Connect to the host & port
            s.connect((host, port))

            # If connection is successful, print the port is open.
            print(f'Port {port} is open')

            # Close the socket
            s.close()
        except:
            # If connection fails / times out, print the port is closed
            print(f'Port {port} is closed')

if __name__ == '__main__':
    # Ask for target host IP to scan
    host = input("Enter the target host IP address: ")

    # Ask for the ports to scan, separated by commas
    ports_str = input("Enter the ports to scan (comma-separated): ")

    # Split the input ports string and convert each port to an integer for scanning
    ports = [int(port.strip()) for port in ports_str.split(',')]

    # Call the port_scanner function with the user-provided target host and ports
    port_scanner(host, ports)
