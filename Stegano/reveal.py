from PIL import Image
import numpy as np

def matrix_multiplication(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    assert cols_A == rows_B,"Cannot multiply the two matrices. Incorrect dimensions."

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


def decode(imageName: str) -> str:
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
        mat = matrix_multiplication(newu, matrix_multiplication(newsig, newv))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                reqchr += str(int(np.round(mat[i][j], 1)))

        output += (chr(int(reqchr, 2)))
    return output
