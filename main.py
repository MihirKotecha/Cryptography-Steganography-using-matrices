from Stegano.hide import encode
from Stegano.reveal import decode

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