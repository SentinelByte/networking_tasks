import subprocess
import ipaddress

def ping_sweep(network):
    # Convert network prefix/CIDR to IP
    ip_net = ipaddress.ip_network(network, strict=False)
    
    # Iterate through all IPs in the network
    for ip in ip_net.hosts():
        # Convert the IP objects to string
        ip = str(ip)
        
        # Capture the ping command output
        result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the ping command was successful (return code 0) and if "1 received" is present in the output
        if result.returncode == 0 and "1 received" in result.stdout:
            # Print IP is up if the ping was successful
            print(ip, 'is up')
        else:
            # Print IP is down if the ping failed or no response was received
            print(ip, 'is down')

if __name__ == '__main__':
    # Prompt the user to enter the network prefix or CIDR notation
    network = input("Enter the network prefix or CIDR notation (e.g., 192.168.1.0/24): ")
    
    # Call the ping_sweep function with the user-provided network input
    ping_sweep(network)
