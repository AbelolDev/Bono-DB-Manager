#Script to generate and store a secure key for fernet encryption. Must be ran on start-up
from cryptography.fernet import Fernet

key = Fernet.generate_key()

# Save it securely — for example, in a .key file
with open('secret.key', 'wb') as key_file:
    key_file.write(key)