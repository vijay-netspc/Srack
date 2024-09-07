line = input().strip().split()
vow = set(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"))
i = 0
for word in line:
    vow_count = sum(1 for letter in word if letter in vow)
    line[i] = [word, vow_count, i]
    i += 1
line.sort(key=lambda x: (-x[1], x[2]))
for word in line:
    print(word[0], end=" ")
