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



def deccrypt(encoded_message):
    string_length = len(encoded_message)

    decoded_message = ""

    for i in range(0,string_length,4):
        A = [[-3,2],[2,-1]]
        chars = encoded_message[i:i+4]
        mat = [[323, 295], [539, 495]]
        C = matrix_multiplication(A,mat)
        print(chars)
        print(C)
        decoded_message += chr(C[0][0])
        decoded_message += chr(C[0][1])
        decoded_message += chr(C[1][0])
        decoded_message += chr(C[1][1])

    print(decoded_message)


deccrypt("âÆȥǭ")

