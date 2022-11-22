from hide import hide_in_image
from reveal import reveal_the_image


def steganography():
    n = int(input(
        "Image Steganography \n1. Encode the data \n2. Decode the data \nSelect the option: "))
    if (n == 1):
        print("\nEncoding...")
        hide_in_image()

    elif (n == 2):
        print("\nDecoding...")
        print("Decoded message is " + reveal_the_image())

    else:
        raise Exception("Inserted value is incorrect!")


# steganography()  # encoding the image
