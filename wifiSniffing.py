import subprocess


def run_netsh_command():
    """Run the 'netsh wlan show networks' command and return the output."""
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            capture_output=True,
            text=True,
            check=True  # Automatically raises CalledProcessError on failure
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error: Failed to execute 'netsh' command.")
        print(f"Details: {e.stderr}")
        return None
    except FileNotFoundError:
        print("Error: 'netsh' command not found. This script only works on Windows.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def parse_networks_output(output):
    """Parse the output of the 'netsh wlan show networks' command."""
    networks = []
    current_network = {}

    for line in output.splitlines():
        line = line.strip()
        if line.startswith("SSID"):
            if "SSID" in current_network:
                networks.append(current_network)
                current_network = {}
            current_network["SSID"] = line.split(":")[1].strip()
        elif line.startswith("Signal"):
            current_network["Signal"] = line.split(":")[1].strip()
        elif line.startswith("Authentication"):
            current_network["Authentication"] = line.split(":")[1].strip()

    # Add the last network to the list if it exists
    if current_network:
        networks.append(current_network)

    return networks


def display_networks(networks):
    """Display the parsed network information in a user-friendly format."""
    if not networks:
        print("No Wi-Fi networks found.")
        return

    print(f"{'SSID':<30} {'Signal':<10} {'Authentication':<20}")
    print("-" * 60)
    for network in networks:
        print(
            f"{network.get('SSID', 'N/A'):<30} {network.get('Signal', 'N/A'):<10} {network.get('Authentication', 'N/A'):<20}"
        )


def probe_new_networks():
    """Main function to probe for and display new networks."""
    print("Probing for new Wi-Fi networks...\n")
    output = run_netsh_command()
    if output:
        networks = parse_networks_output(output)
        display_networks(networks)


if __name__ == "__main__":
    probe_new_networks()