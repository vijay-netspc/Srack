n = int(input())
pre = {} 
for i in range(n):
    word = input().strip()[:3] 
    if word not in pre:
        pre[word] = 1
    else:
        pre[word] += 1 

map_lst = sorted(pre) 
for i in map_lst: 
    print(i, pre[i]) 
