n = int(input())
lst = [int(i) for i in input().strip().split()]
k = int(input())
sub = []
sum1 = float("inf")

for i in range(len(lst)):
    if i + k - 1 < len(lst) and sum(lst[i:i+k]) < sum1:
        sum1 = sum(lst[i:i+k])
        sub = lst[i:i+k]

print(*sub)
