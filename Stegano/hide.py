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
