import socket

def dns_lookup(domain):
    """
    Performs DNS resolution to obtain the IP address of the specified domain and prints it.

    Args:
    - domain: The domain name to perform DNS lookup on.

    Returns:
    - None
    """
    # Get IP associated with the domain using socket.gethostname function
    ip = socket.gethostbyname(domain)
    
    # Print domain IP
    print(f'IP address of {domain} is {ip}')

if __name__ == '__main__':
    # Ask to enter a domain name
    domain = input("Enter the domain name to lookup: ")
    
    # Call the dns_lookup function with the domain provided
    dns_lookup(domain)
