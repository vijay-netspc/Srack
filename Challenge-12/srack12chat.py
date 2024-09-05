from collections import Counter

# Input string
s = input().strip()

# Count frequencies of characters in the string
count_dict = Counter(s)

# Count how many characters have an odd frequency
odd_count = sum(1 for count in count_dict.values() if count % 2 != 0)

# The minimum number of characters to add is odd_count - 1 (if odd_count > 1)
min_additions = max(0, odd_count - 1)

# Output the result
print(min_additions)
