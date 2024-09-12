# Read the input
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

# For each integer X in the first row, print the corresponding Xth row as a column
for j in range(n):
    for i in range(n):
        print(mat[mat[0][i] - 1][j], end=" ")
    print()
