from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64

def generate_key_from_password(password, salt=b'saltsalt'):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# Ask your friend to provide a password
password = input("Enter the password to encrypt the key: ")

# Generate a key from the password
key = generate_key_from_password(password)

# Save the key to a file (e.g., encrypted_key.txt)
with open('encrypted_key.txt', 'wb') as key_file:
    key_file.write(key)

# Encrypt the message using the key
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"This is an encrypted Message for the class: seguridad informatica")

# Save the encrypted message to a file
with open('encrypted_message.txt', 'wb') as encrypted_file:
    encrypted_file.write(cipher_text)