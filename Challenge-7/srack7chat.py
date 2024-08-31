n = int(input())
string = []
for i in range(n):
    temp = input().strip()
    count_in = sum(1 for s in temp if s.islower())
    string.append((temp, count_in, i))

# Sort using the sorted() function with a custom key
string.sort(key=lambda x: (x[1], x[2]))

# Output the sorted strings
for s in string:
    print(s[0])
