from Modules.file_encryption_modules import IsKeyFound, KeyGenerator
from Modules.main_menu import MainMenu

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
        




    

