import subprocess

def trace_the_route(destination):
    """
    Traces the route packets take to reach the specified destination and prints the results.

    Args:
    - destination: The destination IP / Domain name to trace the route to.

    Returns:
    - None
    """
    # Execute the tracert command with the specified destination
    result = subprocess.Popen(['tracert', destination], stdout=subprocess.PIPE)
    
    # Read and print the output of the tracert command
    output = result.communicate()[0]
    print(output.decode())

if __name__ == '__main__':
    # Ask for dest IP / domain
    destination = input("Enter IP / Domain name > ")
    
    # Call the traceroute function with the user-provided destination
    trace_the_route(destination)
