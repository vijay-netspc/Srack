n = int(input())
box = [int(i) for i in input().strip().split()]
box[1] = max(box[0], box[1])
for i in range(2, n):
    box[i] = max(box[i] + box[i-2], box[i-1])
print(box[-1])
