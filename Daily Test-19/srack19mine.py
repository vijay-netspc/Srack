n = int(input())
mat = []
for i in range(n):
    mat.append([int(i) for i in input().strip().split()])
    
for j in range(n):
    for i in mat[0]:
        print(mat[i-1][j], end=" ")
    print(end="\n")
