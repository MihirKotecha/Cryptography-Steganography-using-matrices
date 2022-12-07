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
    Outputs the decoded message from the .tiff image

    Just reversing the process that happened while hiding
    Image --> USV --> 2x4 bit --> binary num --> int --> chr --> string
    """

    # Extracting the pixel array back from the image
    image = Image.open(imageName + ".tiff")
    data = list(image.getdata())

    # from the first 8 items of the array we get the search limit length
    textLen = ""
    for i in range(8):
        textLen += str(int(data[i]))
    ind = 8

    output = "" # will store the output string

    # Iterate through the array till the length of output string
    for rep in range(int(textLen,2)):
        newu = []
        newv = [] 
        newsig = []

        # Extracting back the data
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

        reqchr = ''
        mat = matrix_multiplication(newu, matrix_multiplication(newsig, newv)) #getting back the 8-bit binary data in 2x4 matrix form by multiplying the S,Sig,Vt.
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                reqchr += str(int(np.round(mat[i][j], 1)))

        # Appending each character to get the final string
        output += (chr(int(reqchr, 2)))

    return output # returning the decoded string
