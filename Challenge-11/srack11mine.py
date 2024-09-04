s1 = list(input().strip())
s2 = list(input().strip())
s3 = list(input())

for i in range(len(s1)):
    if s1[i] in s3:
        s3.remove(s1[i])
    else:
        print(s1[i], end="")
        
for i in range(len(s2)):
    if s2[i] in s3:
        s3.remove(s2[i])
    else:
        print(s2[i], end="")
