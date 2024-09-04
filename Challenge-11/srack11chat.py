from collections import Counter

# Take input strings
s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

# Use a Counter to keep track of the frequency of characters in S3
s3_count = Counter(s3)

# Create the result strings
result_s1 = []
result_s2 = []

# Process S1
for ch in s1:
    if s3_count[ch] > 0:
        s3_count[ch] -= 1
    else:
        result_s1.append(ch)

# Process S2
for ch in s2:
    if s3_count[ch] > 0:
        s3_count[ch] -= 1
    else:
        result_s2.append(ch)

# Combine and print the results
print("".join(result_s1) + "".join(result_s2))
