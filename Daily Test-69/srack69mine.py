#Your code below
n=int(input())
lst input().strip().split()
add=0
for i in range(n):
  index=lst[i][::-1].index(min(lst[i]))
  if index!=0: 
    add+=int(lst[i][:-index-1]+lst[i] [-index:]+lst[i][index-1])
  else:
    add+=int(lst[i])
print(add)
