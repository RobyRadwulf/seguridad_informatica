from cryptography.fernet import Fernet
key = Fernet.generate_key()

with open('key.txt', 'wb') as key_file:
    key_file.write(key)

message = b"Hello, Falcon!"
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(message)

with open('encrypted_message.txt', 'wb') as encrypted_file:
    encrypted_file.write(cipher_text)