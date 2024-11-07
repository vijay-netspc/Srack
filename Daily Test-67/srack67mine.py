hr, m, s = list(map(int, input().strip().split(":")))
print("HH:MM:SS")

# print(f"#{hr} #{m} #{s}")
# hr=bin(hr)[2:]
# m=bin(m)[2:]
# s=bin(s)[2:]

#binary = []

def tb(time, num):
    return ("#" * num + bin(time // 10)[2:].zfill(4 - num), bin(time % 10)[2:].zfill(4))

fcol, scol = tb(hr, 2)
tcol, frcol = tb(m, 1)
fvcol, sxcol = tb(s, 1)

for i in range(4):
    print(fcol[i] + scol[i] + " " + tcol[i] + frcol[i] + " " + fvcol[i] + sxcol[i])

# print(fcol, scol, tcol, frcol, fvcol, sxcol)
