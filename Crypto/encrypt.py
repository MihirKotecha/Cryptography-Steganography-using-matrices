def transform(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C


A = [[1,5],[3,2]]
B = [[2,5],[7,6]]

C = transform(A,B)

encode_msg = ""

for i in range(len(C)):
    for j in range(len(C[i])):
        encode_msg += chr((C[i][j])%65)

print(encode_msg)
