# Get IP Address and Hostname of a Website
# Importing socket library
import socket

def get_hostname_IP():
    hostname = input("Please enter website address (URL): ")
    try:
        print(f'Hostname: {hostname}')
        print(f'IP Address: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print(f'Invalid Hostname. Error: {error}')

# Run the function
get_hostname_IP()
