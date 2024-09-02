n = int(input())
box = [int(i) for i in input().strip().split()]

if n == 1:
    print(box[0])
else:
    prev2 = box[0]
    prev1 = max(box[0], box[1])

    for i in range(2, n):
        current = max(box[i] + prev2, prev1)
        prev2 = prev1
        prev1 = current

    print(prev1)
