n=int(input())
nums=[int(i) for i in input().strip().split()]
k=int(input())
for i in nums:
  k=(k-i)%100
  print(k,end=" ")

