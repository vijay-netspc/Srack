n = int(input())
lst = []
for i in range(n):
    lst.append(input().strip())
lst.sort(key = lambda word: -sum(1 for i in word if i.isupper()))
print(*lst, sep = "\n")
