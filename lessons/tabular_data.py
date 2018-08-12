NUM_ROWS = 25
NUM_COLS = 25

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)
 
# print the matrix
for row in my_matrix:
    print(row)
    pass

print(my_matrix[1][4])

# Write a function \color{red}{\verb|trace(matrix)|}trace(matrix) that takes a square matrix \color{red}{\verb|matrix|}
# matrix and returns the value of its trace. Then use your implementation of \color{red}{\verb|trace()|}trace() and 
# compute the value of \color{red}{\verb|trace(my_matrix)|}trace(my_matrix) for instances of my_matrix as defined by 
# the code snippet.   


def trace(matrix):
    column_index = 0
    result = 0
    for row in matrix:
        result += row[column_index]
        column_index += 1
    return result

print(trace(my_matrix))