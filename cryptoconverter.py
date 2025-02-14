import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

def xor_encrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(encoded_text):
    return base64.b64decode(encoded_text.encode()).decode()

def aes_encrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC, iv := os.urandom(16))
    encrypted_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_bytes).decode()

def aes_decrypt(encrypted_text, key):
    raw_data = base64.b64decode(encrypted_text)
    iv, encrypted_bytes = raw_data[:16], raw_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted_bytes), AES.block_size).decode()

def main():
    while True:
        print("\nChoose an operation:")
        print("1. Caesar Cipher Encrypt")
        print("2. Caesar Cipher Decrypt")
        print("3. XOR Encryption")
        print("4. Base64 Encode")
        print("5. Base64 Decode")
        print("6. AES Encrypt")
        print("7. AES Decrypt")
        print("8. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            text = input("Enter text: ")
            shift = int(input("Enter shift: "))
            print("Encrypted text:", caesar_cipher(text, shift, encrypt=True))
        
        elif choice == "2":
            text = input("Enter text: ")
            shift = int(input("Enter shift: "))
            print("Decrypted text:", caesar_cipher(text, shift, encrypt=False))
        
        elif choice == "3":
            text = input("Enter text: ")
            key = input("Enter key: ")
            print("XOR Encrypted text:", xor_encrypt(text, key))
        
        elif choice == "4":
            text = input("Enter text: ")
            print("Base64 Encoded text:", base64_encode(text))
        
        elif choice == "5":
            encoded_text = input("Enter Base64 encoded text: ")
            print("Decoded text:", base64_decode(encoded_text))
        
        elif choice == "6":
            text = input("Enter text: ")
            key = input("Enter 16-byte key: ").encode()
            if len(key) != 16:
                print("Key must be exactly 16 bytes.")
                continue
            print("AES Encrypted text:", aes_encrypt(text, key))
        
        elif choice == "7":
            encrypted_text = input("Enter AES encrypted text: ")
            key = input("Enter 16-byte key: ").encode()
            if len(key) != 16:
                print("Key must be exactly 16 bytes.")
                continue
            print("AES Decrypted text:", aes_decrypt(encrypted_text, key))
        
        elif choice == "8":
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
