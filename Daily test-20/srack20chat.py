from collections import Counter

# Read the input string and split it into words
line = input().strip().split()

# Count the frequency of each word
word_count = Counter(line)

# Find words that are repeated
repeated_words = [word for word in line if word_count[word] > 1]

# Remove duplicates while maintaining order of occurrence
repeated_words = list(dict.fromkeys(repeated_words))

# If no words are repeated, print -1
if not repeated_words:
    print(-1)
else:
    # Sort by length (descending) and maintain order of occurrence
    repeated_words.sort(key=lambda word: -len(word))
    print(*repeated_words)
