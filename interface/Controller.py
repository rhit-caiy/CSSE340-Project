from Ciphers.CrittersCipher import CrittersCipher


class Controller:
    def __init__(self):
        self.plaintext = None
        self.ciphertext = None
        self.key = None
        self.cipher = None

    def promptInput(self):
        print("Please enter a message to encrypt")
        self.plaintext = input()

    def promptEncryptionMethod(self):
        print("Please enter encryption method (1: Critters)")
        choice = input()
        self.key = 100
        if choice == 1:
            self.cipher = CrittersCipher()
        else:
            self.cipher = CrittersCipher

    def runEncryption(self):
        print("encrypting", self.plaintext)
        self.ciphertext = self.cipher.encrypt(self.plaintext, 100)
        print("result", self.ciphertext)
