Project 1: Wifi Sniffer


wifiSniffer.py is a script you can run from the windows cammand line that scans for Wi-Fi networks within range of a Windows device, extracting detailed information such as signal strength, encryption protocols, and authentication methods.


Project 2: Simple Password Brute Force 

SimplePasswordBruteForce.py demonstrates a basic brute-force attack algorithm designed to break a password by systematically guessing all possible combinations of characters. It serves as an example of how brute force attacks function in cybersecurity.

How It Works:

A password must be manually defined in the main method. This is the password the algorithm will attempt to crack.
The max_guess_length variable should be set to the exact length of the password. For example, if the password is abc123, the max_guess_length should be set to 6.

The script will then iterate through all possible character combinations, hash each attempt, and compare it to the hash of the target password. Run the script from the terminal. After running for some time (depending on the complexity of the password), the script will output the original password once it is successfully cracked.

This algorithm is not optimized for real world penetration testing. There are more advanced tools like Hashcat or John the Ripper that are more efficient.

This script is ideal for demonstrating the concept of brute-force attacks and It should only be used in authorized environments and for ethical purposes AKA I am not responsible for what you do with this script though you probably won't get far with it anyways. 

Project 3: Port Scanner

This script scans for ports and can be run in the windows terminal, you need to provide an IP address to target in order for the script to run correctly. 