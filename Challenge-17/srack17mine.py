n = int(input())
arr = [i for i in input().strip().split()]
for i in range(0, n, 3):
    res = arr[i][-1] + arr[i+1][-1] + arr[i+2][-1]
    if res == "000":
        print(-1, end=" ")
        continue
    print(*sorted(res, reverse=True), sep="")
