r, c = [int(i) for i in input().strip().split()]
mat = [[0]*c for _ in range(r)]
n = int(input())

def proc(mat, r1, c1):
    for i in range(r):
        mat[i][c1] ^= 1
    for i in range(c):
        mat[r1][i] ^= 1
    mat[r1][c1] = 1

for _ in range(n):
    r1, c1 = [int(i)-1 for i in input().strip().split()]
    proc(mat, r1, c1)

for row in mat:
    print(*row)
