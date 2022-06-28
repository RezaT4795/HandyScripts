from Modules.File_encryption_modules import KeyGenerator, Encryptor, Decryptor, IsKeyFound
import os    

if IsKeyFound() == False:
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
        




    

