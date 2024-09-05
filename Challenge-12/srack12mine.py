from collections import Counter
s = input().strip()
count_dict = Counter(s)
count = 0
for i in count_dict:
    if count_dict[i] % 2 != 0:
        count += 1

count = count - 1 if (count + len(s)) % 2 == 0 and count > 0 else count
print(count)
