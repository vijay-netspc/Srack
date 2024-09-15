r, c = [int(i) for i in input().split()]

mat = []
for _ in range(r):
    mat.append([int(i) for i in input().strip().split()])

r1, c1 = [int(i) - 1 for i in input().split()]

temp = r1
summ = 0

for _ in range(min(r, c)):
    if r1 == temp and summ == 0:
        break
    summ += mat[r1][c1]
    r1 += 1
    c1 += 1
    
    if r1 >= r or c1 >= c:
        if r1 > c1:
            r1 -= c1
            c1 = 0
        else:
            c1 -= r1
            r1 = 0

print(f"{summ}")
