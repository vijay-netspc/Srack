n = int(input())
og = sorted((int(i) for i in input().strip().split()))
hashmap = set(og)
result = []

for i in range(len(og)):
    for j in range(len(og)):
        if i != j and og[i] + og[j] in hashmap:
            result.append((og[i], og[j], og[i] + og[j]))

if len(result) == 0:
    print(-1)
else:
    result.sort(key=lambda x: (x[2], x[0]))
    for i in result:
        print(f"{i[0]} + {i[1]} = {i[0] + i[1]}")
