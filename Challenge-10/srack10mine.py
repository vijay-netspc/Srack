lst = [int(i) for i in input().strip().split()]
sortlst = sorted(lst)

for i in lst:
    ind = sortlst.index(i) + 1
    if ind < len(lst):
        print(sortlst[ind], end=" ")
    else:
        print(-1, end=" ")
