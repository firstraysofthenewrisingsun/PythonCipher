# Reverse Cipher
# This program takes a string and reverses it, demonstrating an elementary use of cryptography.


class ReverseCipher:
    def __init__(self, message):
        self.message = message

    def reversal(self):
        translated = ''  # Placeholder for reversed string
        i = len(self.message) - 1
        while i > 0:
            translated = translated + self.message[i]
            i = i - 1

            print(i, self.message[i], translated)