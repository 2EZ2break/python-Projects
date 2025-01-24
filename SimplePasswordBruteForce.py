import hashlib
import itertools
import string

def hash_password(password):
    # Hashes a password using SHA-256.
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force(hash_to_crack, max_length):
    # Attempts to crack the hash using a brute-force method. 
    chars = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess_password = ''.join(guess)
            guess_hash = hash_password(guess_password)
            print(f"Trying password: {guess_password} -> {guess_hash}")
            if guess_hash == hash_to_crack:
                return guess_password
    return None

if __name__ == "__main__":
    # Example password: "abc123" can enter your own to test different password
    original_password = "abc123"
    password_hash = hash_password(original_password)

    print(f"Original password hash: {password_hash}")

    # Attempt to crack the hash
    # Max password length is set to 6 and you will neeed to change if you are trying different passwords.
    max_guess_length = 6
    cracked_password = brute_force(password_hash, max_guess_length)

    if cracked_password:
        print(f"Password cracked! The password is: {cracked_password}")
    else:
        print("Failed to crack the password.")
