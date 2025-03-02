import socket
import argparse

# Function to scan ports
def scan_ports(target, ports):
    open_ports = []
    print(f"Scanning target: {target}")
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    return open_ports

def main():
    # Argument parsing for IP/Host and Ports
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("target", help="Target IP or domain name (e.g., 192.168.1.1 or example.com)")
    parser.add_argument(
        "-p", "--ports", 
        default="21,22,23,80,443,8080", 
        help="Comma-separated list of ports to scan (default: 21,22,23,80,443,8080)"
    )
    
    args = parser.parse_args()
    
    # Parse ports
    ports = [int(port) for port in args.ports.split(',')]
    
    # Run port scan
    open_ports = scan_ports(args.target, ports)
    
    # Output results
    if open_ports:
        print(f"Open ports on {args.target}: {open_ports}")
    else:
        print(f"No open ports found on {args.target}.")

if __name__ == "__main__":
    main()