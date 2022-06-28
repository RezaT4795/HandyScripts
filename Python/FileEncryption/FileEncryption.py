from Modules.File_encryption_modules import IsKeyFound, KeyGenerator, Encryptor, Decryptor

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

if IsKeyFound() == False:
    ans = input("No key file found in the current directory.\nDo you want to generate a new private key?(Y/n)")
    if ans in ["y", "Y"]:
        print("Generating a new key...")
        KeyGenerator()
        print("Done!")
        MainMenu()
    else:
        print("Goodbye.")
else:
    print("Private key found.")
    MainMenu()
        




    

