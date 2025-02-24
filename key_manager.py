import os
from cryptography.fernet import Fernet

class KeyManager:
    """Manages encryption key generation and retrieval."""
    
    @staticmethod
    def generate_key():
        """Generate and store encryption key if it does not exist."""
        if not os.path.exists("encryption_key.key"):
            key = Fernet.generate_key()
            with open("encryption_key.key", "wb") as key_file:
                key_file.write(key)
        return KeyManager.load_key()

    @staticmethod
    def load_key():
        """Load encryption key from file."""
        try:
            with open("encryption_key.key", "rb") as key_file:
                return key_file.read()
        except FileNotFoundError:
            return None
