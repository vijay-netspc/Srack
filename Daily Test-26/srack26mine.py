s = input().strip()
k = int(input())
hash_map = {}
for i in range(0, len(s) - k + 1):
    hash_map[s[i:i + k]] = hash_map.get(s[i:i + k], 0) + 1
for key in hash_map:
    print(key, hash_map[key])
