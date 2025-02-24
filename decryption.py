import cv2
from cryptography.fernet import Fernet
from key_manager import KeyManager

class Decryptor:
    """Handles message decryption and image decoding."""

    def __init__(self):
        self.key = KeyManager.load_key()
        self.cipher = Fernet(self.key) if self.key else None

    def decrypt_message(self, encrypted_message):
        """Decrypts the encrypted message."""
        if not self.cipher:
            return "❌ Error: Encryption key missing!"
        decrypted_message = self.cipher.decrypt(encrypted_message.encode()).decode()
        return decrypted_message

    def decode_image(self, image_path):
        """Extracts encrypted data from an image."""
        image = cv2.imread(image_path)
        if image is None:
            return "❌ Error: Invalid image file!"

        binary_data = ""

        for row in image:
            for pixel in row:
                for channel in range(3):
                    binary_data += str(pixel[channel] & 1)

        bytes_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
        extracted_data = ''.join([chr(int(byte, 2)) for byte in bytes_data])

        if '####' in extracted_data:
            return extracted_data.split('####')[0]
        return None
