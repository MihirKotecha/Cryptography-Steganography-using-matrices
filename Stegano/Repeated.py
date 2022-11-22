import numpy as np

def msg_to_bin(msg):
    if type(msg) == str:
        return [format(ord(i), "08b") for i in msg]
    elif type(msg) == bytes or type(msg) == np.ndarray:
        return [format(i, "08b") for i in msg]
    elif type(msg) == int or type(msg) == np.uint8:
        return format(msg, "08b")
    else:
        raise TypeError("Input type not supported")
    return

def getSVD(matrix):
    return np.linalg.svd(matrix)