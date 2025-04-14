                                                                                                         
import getpass
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Initialize the password hasher
ph = PasswordHasher()

def hash_password(password: str):
    """Generates an Argon2id hash from the password."""
    return ph.hash(password)

def verify_input_password(user_input: str, stored_hash: str):
    """
    Verifies if the user input matches the stored hash.
    This uses Argon2's built-in verification (handles salt internally).
    """
    try:
        return ph.verify(stored_hash, user_input)
    except VerifyMismatchError:
        return False

def main():
    print("Argon2 Password Hashing & Verification")

    # stored hash (of the correct password: 'senaya')
    stored_hash = "$argon2id$v=19$m=102400,t=2,p=8$yfS9D106E6BoFt245/w/6A$rVNSgAGuEbW4JSEiUFIwgw"

    # Ask user for a password (hidden input)
    user_input = getpass.getpass("Enter your password: ")

    # Hash the user input and display it
    user_hash = hash_password(user_input)
    print(f"\nYour generated hash:\n{user_hash}\n")

    # Check if the input matches the stored hash
    if verify_input_password(user_input, stored_hash):
        print("Password verification successful!")
    else:
        print("Password verification failed.")

if __name__ == "__main__":
    main()

