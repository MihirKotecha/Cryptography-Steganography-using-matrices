from Stegano.hide import encode
from Stegano.reveal import decode
from Crypto.encrypt import encrypt
from Crypto.decrypt import deccrypt



mode = int(input("Enter 1 to use Cryptography or Enter 2 to use Steganogarphy: "))

if(mode == 1):
    n = int(input("Enter 1 to Encrypt and 2 to Decrypt: "))

    if(n == 1):
        cipher = input("Enter the message you want to encrypt: ")
        print("The Encrypted message is: ",encrypt(cipher))
    
    elif(n == 2):
        decipher = input("Enter the encrypted message to be decrypted: ")
        print("Your message is: ",deccrypt(decipher))
    
    else:
        print("Try again !")


elif(mode == 2):

    n = int(input("Enter 1 to hide and 2 to reveal: "))

    if(n == 1):
        cipher = input("Enter the text: ")
        imageName = input("Enter the image name: ")
        try:
            encode(text = cipher,imageName = imageName)
            print("Encoded sucessfully")
        except Exception as e:
            print("Error occured",str(e))


    elif(n == 2):
        try:
            imageName = input("Enter the image name (without .tiff): ")
            print("The Decoded message is: ",decode(imageName=imageName))
        except Exception as e:
            print("Error occured",str(e))

    else:
        print("Try Again!")
else:
    print("Please try again !")