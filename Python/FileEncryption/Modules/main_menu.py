from Modules.file_encryption_modules import Encryptor, Decryptor

def MainMenu():
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