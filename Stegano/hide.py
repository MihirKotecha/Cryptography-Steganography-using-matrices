from PIL import Image
import numpy as np


def encode(text:str, imageName:str):
    """
    This function takes in:
    the text that needs to be ciphered.
    the image name.
    Outputs the image with hidden text

    Idea: SVD (Singular value decomposition)
    Input: Word
    string --> chr --> Ascii --> int --> binary(8 bit) --> 2X4 matrix of bit --> U 2x2,S 2x4,V 4x4 --> Image
    """

    # base pixel values of image. 1-D array of just black and white intensties
    data = np.random.uniform(low=-255, high=255, size=(100*len(text),)) # creates a numpy array with random float values between -255 to 255

    ind = 0 # helps in traversing through the array

    textLen = format((len(text)),'08b') # gets binary number of the lenght of the string to be encoded
    
    # inserting the 8-bit binary number into the array of image, to define a breaking point of search in reveal
    for i in range(8):
        data[ind] = int(textLen[i])
        ind+=1

    # Iterarting through each character and putting its SVD values into the array
    for ch in text:

        # ASCII --> binary
        b = format((ord(ch)),'08b')

        #binary --> 2x4 Matrix
        b1 = [int(i) for i in b[0:4]]
        b2 = [int(i) for i in b[4:]]
        mat = np.array([b1, b2])

        #2x4 Matrix to U 2x2,S 2x4,V 4x4
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

        # Saving those values in Pixel array
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
                

    # Creating an image that retains the data with accuracy
    img=Image.fromarray(data)
    img.save(imageName + ".tiff")
    return 
