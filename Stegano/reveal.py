
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
