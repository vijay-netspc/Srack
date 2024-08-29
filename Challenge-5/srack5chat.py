r, c = [int(i) for i in input().strip().split()]
lst = []
for i in range(r):
    lst.append([0 if ch == '-' else ch for ch in input().strip().split()])

if lst[r-1][c-1] == '*':  # If the start is an obstacle
    print(0)
else:
    lst[r-1][c-1] = 1  # Set the bottom-right corner to 1

    for i in range(r-1, -1, -1):
        for j in range(c-1, -1, -1):
            if lst[i][j] != "*":
                if i + 1 < r and lst[i+1][j] != "*":
                    lst[i][j] += lst[i+1][j]
                if j + 1 < c and lst[i][j+1] != "*":
                    lst[i][j] += lst[i][j+1]

    print(lst[0][0])
