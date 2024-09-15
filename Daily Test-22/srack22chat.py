r, c = map(int, input().split())

# Initialize the matrix
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))

# Read the position of the cell
m, n = map(int, input().split())

# Convert to zero-based indexing
m -= 1
n -= 1

# Calculate the starting point of the diagonal
start_row = m - min(m, n)
start_col = n - min(m, n)

# Initialize sum
diagonal_sum = 0

# Traverse the diagonal
while start_row < r and start_col < c:
    diagonal_sum += matrix[start_row][start_col]
    start_row += 1
    start_col += 1

# Print the result
print(diagonal_sum)
