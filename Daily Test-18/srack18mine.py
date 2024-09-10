n = int(input())
res = set()
for i in range(n):
    if i == 0:
        res = set(input().strip().split())
        continue
    res &= set(input().strip().split())
print(len(res))
