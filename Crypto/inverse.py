import random

def getRandomMatrix(rows, cols):
    matrix = []
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(random.randint(1,100))
        matrix.append(temp)
    return matrix

matrix = getRandomMatrix(2,2)
for i in matrix:
    print(*i)



# bench testing the code
