#  Caesar Cipher
#  Encrypts keys by using a predefined Encryption/Decryption Key as the offset amount.
import random


class CaesarCipher:
    key = 0
    mode = ''
    message = ''

    def __init__(self):
        self.LETTERS = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] ' \
                       '^_`abcdefghijklmnopqrstuvwxyz{|}~ '
        # Number used to randomize encryption output
        self.rand = random.randint(1, 26)
        self.from_user_input()

    # Gathers user input
    def from_user_input(self):
        key = int(input('Enter Key: '))
        mode = input('E:Encrypt / D:Decrypt: ')
        message = input('Message to be modified: ')
        self.data_input(key, mode, message, self.rand)

    #  Assigns input to appropriate methods
    def data_input(self, key, mode, message, rand):
        check = True
        while check:

            #  Initiates Encryption function
            if mode == 'E':
                encrypt = self.run_encrypt(key, message, rand)
                print('Using rand:', self.rand, 'Encrypted Word: ', encrypt)
                response_1 = input('Decrypt Text? Y/N: ')
                if response_1 == 'Y':
                    decrypt = self.run_decrypt(key, encrypt, rand)
                    print(decrypt)
                else:
                    print('GoodBye!')
                    check = False

            #  Initiates Decryption function
            elif mode == 'D':
                decrypt = self.init_decrypt(key, message, rand)
                print(decrypt + '\n')

                response_2 = input('Encrypt More Text? Y/N: ')

                if response_2 == 'Y':
                    key = int(input('Enter Key: '))
                    message = input('Message to be modified: ')
                    encrypt = self.init_encrypt(key, message, random.randint)
                    print(encrypt)
                else:
                    print('GoodBye!')
                    check = False

    #  Encrypts string
    def run_encrypt(self, key, message, rand):
        translated = ''
        for symbol in range(len(message)):
            letter = message[symbol]
            if letter in self.LETTERS:
                translated += chr((ord(letter) + key) % 26)
            else:
                pass
        return translated

    #  Decrypts string
    def run_decrypt(self, key, message):
        translated = ''
        letters = ''
        for symbol in range(len(message)):
            letter = message[symbol]
            if letters in self.LETTERS:
                translated += chr((ord(letter) - key) % 26)
            else:
                pass
        return translated
