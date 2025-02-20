import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

class BlackoutCrypto:
    def __init__(self):
        self.__SECRETS_DIR = 'secrets'
        self.__PRIVATE_KEY_FILE = os.path.join(self.__SECRETS_DIR, 'private_key.pem')
        self.__PUBLIC_KEY_FILE = os.path.join(self.__SECRETS_DIR, 'public_key.pem')

        # Ensure the secrets directory exists
        if not os.path.exists(self.__SECRETS_DIR):
            os.makedirs(self.__SECRETS_DIR)

        # Load or generate the key pair
        self.private_key, self.public_key = self.__load_or_generate_keys()

    def __load_or_generate_keys(self):
        """Load the key pair from files or generate a new pair if they don't exist."""
        if os.path.exists(self.__PRIVATE_KEY_FILE) and os.path.exists(self.__PUBLIC_KEY_FILE):
            with open(self.__PRIVATE_KEY_FILE, 'rb') as key_file:
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                )
            with open(self.__PUBLIC_KEY_FILE, 'rb') as key_file:
                public_key = serialization.load_pem_public_key(
                    key_file.read(),
                )
        else:
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
            )
            public_key = private_key.public_key()

            # Save the private key
            with open(self.__PRIVATE_KEY_FILE, 'wb') as key_file:
                key_file.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                ))

            # Save the public key
            with open(self.__PUBLIC_KEY_FILE, 'wb') as key_file:
                key_file.write(public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))

        return private_key, public_key

    def encrypt(self, message):
        """Encrypt a message using the public key."""
        if not isinstance(message, bytes):
            message = message.encode()
        encrypted_message = self.public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_message

    def decrypt(self, encrypted_message):
        """Decrypt a message using the private key."""
        decrypted_message = self.private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_message.decode()  # Convert bytes back to string

    def get_public_key(self):
        """Return the public key (for external use if needed)."""
        return self.public_key

    def get_private_key(self):
        """Return the private key (for external use if needed)."""
        return self.private_key