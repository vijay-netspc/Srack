# Your code below
n = int(input())
fac = [i for i in range(1, n+1) if n % i == 0]

for i in range(len(fac)):
    for j in range(i):
        print(fac[j], end=" ")
    print(f"{fac[i]} " * (len(fac) - i))
