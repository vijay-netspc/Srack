line = input().strip().split()
words = []
for i, j in enumerate(line):
    if j in line[i+1:] and j not in words:
        words.append(j)
if len(words) == 0:
    print(-1)
else:
    print(*sorted(words, key=lambda word: -len(word)))
