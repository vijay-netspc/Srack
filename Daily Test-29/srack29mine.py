n = int(input())
seconds = [int(i) for i in input().strip().split()]
x = int(input())
ng = x
for i in range(len(seconds) - 1):
    if seconds[i] + x - 1 >= seconds[i + 1]:
        ng += seconds[i + 1] - seconds[i]
    else:
        ng += x
print(ng)
