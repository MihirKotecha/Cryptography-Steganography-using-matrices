<<<<<<< HEAD
# importing the required libraries
import cv2
from Repeated import msg_to_bin


def hide_in_image():
    img_name = input("Enter image name (with Extension): ")
    # reading the input image using OpenCV-Python
    img = cv2.imread(img_name)

    # printing the details of the image
    # checking the image shape to calculate the number of bytes in it
    print("The shape of the image is: ", img.shape)

    data = input("Enter data to be encoded: ")
    assert len(data) > 0, "Data is Empty"

    encodedImage = hide_data(img, data)
    # file_name = input(
    #     "Enter the name of the new encoded image (with extension): ")
    # # calling the hide_data() function to hide the secret message into the selected image
    # cv2.imwrite(file_name, encodedImage)
    return

# converting types to binary


def hide_data(img, secret_msg):
    # calculating the maximum bytes for encoding
    # image rows X image columns X 3 colors X 8 bits
    nBytes = img.shape[0] * img.shape[1] * 3 // 8
    print("Maximum Bytes for encoding:", nBytes)
    # checking whether the number of bytes for encoding is less
    # than the maximum bytes in the image
    assert len(
        secret_msg) <= nBytes, "Error encountered insufficient bytes, need bigger image or less data !!"
    assert len(
        secret_msg) >= 8, "Secret is to small"
    dataIndex = 0
    # converting the input data to binary format using the msg_to_bin() function
    bin_secret_msg = msg_to_bin(secret_msg)
    print("Secret in binary is: ", bin_secret_msg)

    # finding the length of data that requires to be hidden
    dataLen = len(bin_secret_msg)

    breakFlag = False
    for values in img:
        for pixels in values:
            # converting RGB values to binary format
            r, g, b = msg_to_bin(pixels)
            dataIndex += 1
            if(dataIndex > dataLen):
                pixels[2] = 1
                breakFlag = True
                break
        if(breakFlag):
            break

    return img


hide_in_image()
=======

from PIL import Image
import numpy as np


def encode(text:str, imageName:str):
    """
    This function takes in:
    the text that needs to be ciphered.
    the image name.
    """
    data = np.random.uniform(low=-255, high=255, size=(100*len(text),))
    ind = 0
    textLen = format((len(text)),'08b')
    # print(textLen)
    for i in range(8):
        data[ind] = int(textLen[i])
        ind+=1
    for ch in text:
        # print(bin(ord(ch)))
        b = format((ord(ch)),'08b')
        b1 = [int(i) for i in b[0:4]]
        b2 = [int(i) for i in b[4:]]
        mat = np.array([b1, b2])

        u, s, v = np.linalg.svd(mat)
        # print("THE SVD")
        # print(u, s, v)
        S = []

        # create m x n Sigma matrix
        for i in range(len(mat)):
            tmp = []
            for j in range(len(mat[0])):
                if (i == j):
                    try:
                        tmp.append(s[i])
                    except:
                        tmp.append(0)
                else:
                    tmp.append(0)
            S.append(tmp)
        # reconstruct matrix
        S = np.array(S)

        for i in range(2):
            for j in range(2):
                data[ind] = u[i][j]
                ind+=1

        for i in range(2):
            for j in range(4):
                data[ind] = S[i][j]
                ind+=1

        for i in range(4):
            for j in range(4):
                data[ind] = v[i][j]
                ind+=1
                


    img=Image.fromarray(data)
    img.save(imageName + ".tiff")
    return 
>>>>>>> 038e196 (Demo Stegano)
