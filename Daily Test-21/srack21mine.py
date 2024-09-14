n = input().strip()
p = int(input())
q = input().strip()
count = 0
for i in range(p):
    n = str(int(n) + p)
    if q in n:
        count += 1
print(f"{count}")
