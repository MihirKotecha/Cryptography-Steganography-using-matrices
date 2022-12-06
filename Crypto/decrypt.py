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
        mat = [[ord(chars[0]), ord(chars[1])], [ord(chars[2]), ord(chars[3])]]
        C = matrix_multiplication(A,mat)
        print(chars)
        print(C)
        for i in range (2):
            for j in range (2):
                if(C[i][j]!=95):
                    decoded_message += chr(C[i][j])

    return decoded_message


print(deccrypt("ĽĻȒȍİĝȁǛ"))