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

password = input("Enter the password to decrypt the key: ")

with open('encrypted_key.txt', 'rb') as key_file:
    encrypted_key = key_file.read()

key = generate_key_from_password(password)

cipher_suite = Fernet(key)

with open('encrypted_message.txt', 'rb') as encrypted_file:
    cipher_text = encrypted_file.read()

plain_text = cipher_suite.decrypt(cipher_text)

print("Decrypted Message:", plain_text.decode())