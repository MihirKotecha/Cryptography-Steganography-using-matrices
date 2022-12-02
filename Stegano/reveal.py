<<<<<<< HEAD
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
=======

from PIL import Image
import numpy as np

def decode(imageName: str):
    """
    This function decodes the text hidden inside the image
    """
    image = Image.open(imageName + ".tiff")
    data = list(image.getdata())
    textLen = ""
    for i in range(8):
        textLen += str(int(data[i]))
    ind = 8
    # print(textLen)
    output = ""
    for rep in range(int(textLen,2)):
        newu = []
        newv = []
        newsig = []

        for i in range(2):
            tmp = []
            for j in range(2):
                tmp.append(data[ind])
                ind+=1
            newu.append(tmp)

        for i in range(2):
            tmp = []
            for j in range(4):
                tmp.append(data[ind])
                ind+=1
            newsig.append(tmp)

        for i in range(4):
            tmp = []
            for j in range(4):
                tmp.append(data[ind])
                ind+=1
            newv.append(tmp)

        newu = np.array(newu)
        newv = np.array(newv)
        newsig = np.array(newsig)

        reqchr = ''
        mat = newu.dot(newsig.dot(newv))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # print(int(np.round(mat[i][j], 1)),end=" ")
                reqchr += str(int(np.round(mat[i][j], 1)))
            # print()

        output += (chr(int(reqchr, 2)))
    return output
>>>>>>> 038e196 (Demo Stegano)
