def sort_submatrices(matrix, R, C):
    submatrices = []
    
    # Extracting 2x2 submatrices
    for i in range(0, R, 2):
        for j in range(0, C, 2):
            submatrix = [
                [matrix[i][j], matrix[i][j+1]],
                [matrix[i+1][j], matrix[i+1][j+1]]
            ]
            submatrices.append((matrix[i][j], submatrix))  # Store top-left value and submatrix
    
    # Sorting the submatrices based on top-left element (automatically maintains order of occurrence)
    submatrices.sort(key=lambda x: x[0])
    
    # Place sorted submatrices back into the matrix
    idx = 0
    for i in range(0, R, 2):
        for j in range(0, C, 2):
            matrix[i][j], matrix[i][j+1] = submatrices[idx][1][0]
            matrix[i+1][j], matrix[i+1][j+1] = submatrices[idx][1][1]
            idx += 1

    return matrix

# Input
R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

# Process
sorted_matrix = sort_submatrices(matrix, R, C)

# Output
for row in sorted_matrix:
    print(' '.join(map(str, row)))
