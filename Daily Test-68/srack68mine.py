#Your code below
import math
n=int(input())
# print(n*5+(5-(n//2)%5)%5)
keys={1:5,2:4,3:9,4:3,5:8,6:2,7:7,8:1,9:6,0:0}
def compress(n):
    if len(n)==1:
        return int(n)%10
    elif len(n)==2:
        return int(n[-1])+int(n[-2])-1 if int(n[-2])%2==1 else int(n[-1])+int(n[-2])
    else:
        return compress(n[:-2]+str(compress(n[-2]+n[-1])))
#temp=(n%10+(n//10)%10)%10

#if (n//10)%2==1:
#    temp-=1
#print(keys[temp])
print((n//2)*10+keys[compress(str(n))%10])
