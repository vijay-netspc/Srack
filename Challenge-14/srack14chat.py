line = input().strip().split()
vowels = set("aeiouAEIOU")

# Sort by vowel count in descending order, and use Python's stable sorting to maintain the original order
line.sort(key=lambda word: -sum(1 for letter in word if letter in vowels))

# Print the words, joined by space
print(" ".join(line))
