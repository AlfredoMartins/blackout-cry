from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import os

class BlackoutCrypto:
    def __init__(self):
        self.__PRIVATE_FILE_NAME = 'secrets/key.pem'
        self.__PUBLIC_FILE_NAME = 'secrets/key.pub'
        
        self.public_key = None
        self.private_key = None

    def __generate_key(self, file_name):
        self.key = RSA.generate(2048)
        with open(file_name, 'wb') as f:
            f.write(self.key.export_key('PEM'))
        return self.key

    def generate_keys(self):
        self.private_key = self.__generate_key(self.PRIVATE_FILE_NAME)
        self.public_key = self.private_key.publickey()
        with open(self.PUBLIC_FILE_NAME, 'wb') as f:
            f.write(self.public_key.export_key('PEM'))
        return self.public_key, self.private_key

    def load_keys(self):
        self.public_key = self.__load_key(self.PUBLIC_FILE_NAME)
        self.private_key = self.__load_key(self.PRIVATE_FILE_NAME)
        return self.public_key, self.private_key

    def __load_key(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'rb') as file:
                key = RSA.import_key(file.read())
                return key
        return None

    def encrypt(self, message):
        if not self.public_key:
            self.load_keys()
        cipher = PKCS1_OAEP.new(self.public_key)
        cipher_text = cipher.encrypt(message.encode())
        return cipher_text

    def decrypt(self, cipher_text):
        if not self.private_key:
            self.load_keys()
        cipher = PKCS1_OAEP.new(self.private_key)
        message = cipher.decrypt(cipher_text)
        return message.decode()

    def get_public_key(self):
        if not self.public_key:
            self.load_keys()
        return self.public_key