def transform(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C


message = input("Enter the message to be encoded: ")
string_length = len(message)

if(string_length%4 != 0):
    while(string_length%4 != 0):
        space = "_"
        message = message + space
        string_length = len(message)
        print("Adding space")

encoded_message = ""

for i in range(0,string_length,4):
    A = [[3,4],[5,6]]
    chars = message[i:i+4]
    mat = [[ord(chars[0]), ord(chars[1])], [ord(chars[2]), ord(chars[3])]]
    C = transform(A,mat)
    encoded_message += chr(C[0][0]-97)
    encoded_message += chr(C[0][1]-97)
    encoded_message += chr(C[1][0]-97)
    encoded_message += chr(C[1][1]-97)
    


print(encoded_message)


        




# A = [[1,5],[3,2]]
# B = [[2,5],[7,6]]

# C = transform(A,B)

# encode_msg = ""

# for i in range(len(C)):
#     for j in range(len(C[i])):
#         encode_msg += chr((C[i][j])%65)

# print(encode_msg)
