import cv2
import os
from cryptography.fernet import Fernet
from key_manager import KeyManager

class Encryptor:
    """Handles message encryption and image encoding."""

    def __init__(self):
        self.key = KeyManager.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_message(self, message):
        """Encrypts a message."""
        encrypted_message = self.cipher.encrypt(message.encode())
        return encrypted_message.decode()  # Convert bytes to string

    def encode_image(self, image_path, secret_data):
        """Encodes encrypted data into an image (PNG, JPG, JPEG)."""
        image = cv2.imread(image_path)
        if image is None:
            return "❌ Error: Invalid image file!", None

        data = secret_data + '####'  # End delimiter
        binary_data = ''.join(format(byte, '08b') for byte in data.encode())

        h, w, _ = image.shape
        max_bytes = h * w * 3 // 8  # Max capacity

        if len(binary_data) > max_bytes:
            return "❌ Error: Message too large for this image!", None

        # Encode binary data into pixels
        data_index = 0
        for row in image:
            for pixel in row:
                for channel in range(3):
                    if data_index < len(binary_data):
                        pixel[channel] = (pixel[channel] & ~1) | int(binary_data[data_index])
                        data_index += 1

        # Save encoded image
        output_path = os.path.splitext(image_path)[0] + "_encoded.png"
        cv2.imwrite(output_path, image, [cv2.IMWRITE_PNG_COMPRESSION, 9])
        
        return f"✅ Data successfully encoded in '{output_path}'", output_path

