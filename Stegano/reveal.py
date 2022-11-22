import cv2
from Repeated import msg_to_bin

def reveal_the_image():
    # reading the image containing the hidden image
    img_name = input(
        "Enter the name of the Steganographic image that has to be Revealed (with extension): ")
    img = cv2.imread(img_name)  # reading the image using the imread() function

    print("The Steganographic image is as follow: ")
    text = show_data(img)
    return text


def show_data(img):
    bin_data = ""
    for values in img:
        for pixels in values:
            # converting the Red, Green, Blue values into binary format
            r, g, b = msg_to_bin(pixels)
    # split by 8-Bits
    allBytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]
    # converting from bits to characters
    decodedData = ""
    for bytes in allBytes:
        decodedData += chr(int(bytes, 2))
    print(decodedData)
    # removing the delimiter to display the actual hidden message
    return decodedData