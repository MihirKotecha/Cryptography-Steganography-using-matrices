from Stegano.hide import encode
from Stegano.reveal import decode
from Crypto.encrypt import encrypt
from Crypto.decrypt import deccrypt


#User can select between Cryptograhy and Steganography
mode = int(input("Enter 1 to use Cryptography or Enter 2 to use Steganogarphy: "))

# for Cryptography
if(mode == 1):

    # Select between Encryption and Decryption
    n = int(input("Enter 1 to Encrypt and 2 to Decrypt: "))

    #for Encrypting
    if(n == 1):

        cipher = input("Enter the message you want to encrypt: ") #taking in the text to be encrypted

        print("The Encrypted message is: ",encrypt(cipher)) #Printing the Encrypted text
    
    #for Decrypting
    elif(n == 2):

        decipher = input("Enter the encrypted message to be decrypted: ") #taking in the text to be decrypted

        print("Your message is: ",deccrypt(decipher)) #Printing the Decrypted text
    
    # Errors
    else:

        print("Try again !") 

# for Steganography
elif(mode == 2):

    # Select between Hiding and Revealing
    n = int(input("Enter 1 to hide and 2 to reveal: "))

    #for Hiding
    if(n == 1):

        cipher = input("Enter the text: ") # taking in the text to be hidden

        imageName = input("Enter the image name: ") # the image name in which the text will be hidden

        try:

            encode(text = cipher,imageName = imageName) #Encoding
            print("Encoded sucessfully")

        except Exception as e:

            print("Error occured",str(e)) # Errors

    #for Revealing
    elif(n == 2):

        try:

            imageName = input("Enter the image name (without .tiff): ") #inputing the image with hidden data
            print("The Decoded message is: ",decode(imageName=imageName))  #printing the Decoded message

        except Exception as e:

            print("Error occured",str(e)) # Errors

    else:
        print("Try Again!") # Errors

# for Errors
else:
    print("Please try again !")