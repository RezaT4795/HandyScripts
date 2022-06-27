from cryptography.fernet import Fernet
import os
import os.path

def KeyGenerator():
        # Generating the key
        key = Fernet.generate_key()
        # Exporting the key to a file
        with open('private.key', 'wb') as EncryptionKey:
            EncryptionKey.write(key)

def Encryptor(PrivKey, file):
    # Reading the generated key and using it
    with open(PrivKey, 'rb') as EncryptionKey:
        key = EncryptionKey.read()
    KeyHolder = Fernet(key)

    # Reading the original file
    with open(file, 'rb') as OriginalFile:
        org = OriginalFile.read()

    # Encrypting the content
    encrypted = KeyHolder.encrypt(org)

    # Writing to the file
    with open(file, 'wb') as EncryptedFile:
        EncryptedFile.write(encrypted)
        
def Decryptor(PrivKey, file):
    # Reading the encrypted file
    with open(file, 'rb') as EncryptedFile:
        enc = EncryptedFile.read()
        
    # Reading the generated key and using it
    with open(PrivKey, 'rb') as EncryptionKey:
        key = EncryptionKey.read()
    KeyHolder = Fernet(key)
    
    # Decrypting the file
    decrypted = KeyHolder.decrypt(enc)
    
    # Writing to the file
    with open(file, 'wb') as EncryptedFile:
        EncryptedFile.write(decrypted)
    

if os.path.exists("./private.key") == False:
    ans = input("No key file found in the current directory.\nDo you want to generate a new private key?(Y/n)")
    if ans == "y" or "Y":
        print("Generating a new key...")
        KeyGenerator()
        print("Done!")
else:
    print("Private key found.")
    pass

print("What do you want to do?\n 1. Encryption\n 2. Decryption")
prompt = input(":")
if prompt == "1":
    print("Encrypting...")
    Encryptor('private.key','new.txt')
    print("Done!")
elif prompt == "2":
    print("Decrypting...")
    Decryptor('private.key','new.txt')
    print("Done!")
else:
    "Input Error."
        




    

