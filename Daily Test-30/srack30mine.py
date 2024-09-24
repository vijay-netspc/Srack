r,c=[int(i) for i in input().strip().split()]
mat2=[]
for i in range(r//2):
    row1=[int(i) for i in input().strip().split()]
    row2=[int(i) for i in input().strip().split()]
    # print(row1, row2)
    for i in range(0, c, 2):
        mat2.append((row1[i:i+2], row2[i:i+2]))
mat2.sort(key=lambda x: x[0][0])
# for x2 in mat2:
    # print(x2)
# print("ans")
for i in range(0, len(mat2), c//2):
    for j in range(c//2):
        print(*mat2[i+j][0], end=" ")
    print(end="\n")
    for j in range(c//2):
        print(*mat2[i+j][1], end=" ")
    print(end="\n")
