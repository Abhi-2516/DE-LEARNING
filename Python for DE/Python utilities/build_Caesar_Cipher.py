# """
# Building a Caesar Cipher

# Challenge: Secret Message Encryptor & Decryptor

# Create a Python script that helps you send secret messages to your friend using simple encryption.

# Your program should:
# 1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
# 2. If encrypting:
#    - Ask for a message and a numeric secret key.
#    - Use a Caesar Cipher (shift letters by the key value).
#    - Output the encrypted message.
# 3. If decrypting:
#    - Ask for the encrypted message and key.
#    - Reverse the encryption to get the original message.

# Rules:
# - Only encrypt letters; leave spaces and punctuation as-is.
# - Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

# Bonus:
# - Allow uppercase and lowercase letter handling
# - Show a clean interface
# """

def encrypt(message , key):
    result = ""
    
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            
            result += chr(shifted)
        

        else:
            result += char
    
    return result


def decrypt(message ,key):
    return encrypt(message , -key)

print("Secret message")

choice = input("DO yopu want to E OR D").strip().lower()

if choice == 'e':
    text = input("enter your message : ")
    try:
        key = int(input("enter an key for enryption "))
        encrypted = encrypt(text, key)
        
        print(f"encrypted message is :  {encrypted}")
        
    except ValueError:
        print("Invalid key")
        
else:
    if choice == 'e':
        text = input("enter your decrypted  message : ")
        try:
            key = int(input("enter an key for enryption "))
            dencrypted = decrypt(text, key)
            
            print(f"encrypted message is :  {dencrypted}")
            
        except ValueError:
            print("Invalid key")