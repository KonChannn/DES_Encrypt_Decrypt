# main.py

from des import *
from util import *
import base64

def main():
    # Input choice for encrypt or decrypt
    choice = input("Do you want to (1) Encrypt or (2) Decrypt? Enter 1 or 2: ").strip()

    if choice == '1':
        # Encrypt flow
        plaintext = input("Enter the plaintext: ").strip()

        # Pad the user input with zeros
        padded_plaintext = pad_string(plaintext)

        key = input("Enter the 64-bit key: ").strip()

        ciphertext = encryption(padded_plaintext, key)
        # print(enc_base64, len(enc_base64))
        print("Ciphertext: ", ciphertext, len(ciphertext))

        # print("Ciphertext:" + ciphertext)

    elif choice == '2':
        # Decrypt flow
        ciphertext = input("Enter the ciphertext: ").strip()
        key = input("Enter the 64-bit key: ").strip()

        decrypted_text = decryption(ciphertext, key)

        # rstrip('0) to remove the zeros padding
        print("Decrypted plaintext: ", decrypted_text.rstrip('1'))

    else:
        print("Invalid choice! Please enter 1 for encryption or 2 for decryption.")

if __name__ == "__main__":
    main()