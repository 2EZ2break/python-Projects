import os

# List of important /etc files to check
files_to_check = [
    "/etc/passwd",               # User info
    "/etc/os-release",           # OS info
    "/etc/alpine-release",       # Alpine version info
    "/etc/hostname",             # Hostname of the system
    "/etc/hosts",                # Local DNS and IP mapping
    "/etc/crontab",              # Cron jobs info
    "/etc/group",                # Group info
    "/etc/sudoers",              # Sudoers file (permissions)
    "/etc/network/interfaces",   # Network config
    "/etc/ssh/sshd_config",      # SSH server config
]

# Function to check file and store content
def check_file(file_path, output_file):
    output_file.write(f"\n[+] Checking {file_path}\n")
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                output_file.write(f"Content of {file_path}:\n")
                output_file.write(file.read() + "\n")
        except PermissionError:
            output_file.write(f"[-] Permission denied for {file_path}\n")
    else:
        output_file.write(f"[-] File {file_path} not found.\n")

# Main function to enumerate files and store in a text file
def enumerate_etc_files():
    # Open the output file in write mode
    with open("etc_enumeration_output.txt", "w") as output_file:
        for file in files_to_check:
            check_file(file, output_file)

if __name__ == "__main__":
    enumerate_etc_files()
    print("Enumeration complete. Results saved to 'etc_enumeration_output.txt'.")