# Input the number of strings
n = int(input())

# Initialize an empty set for the common words
res = set()

# Loop through the input strings
for i in range(n):
    # Input each string and split it into words
    words = set(input().strip().split())
    
    # For the first string, initialize the result set with its words
    if i == 0:
        res = words
    else:
        # For subsequent strings, find the intersection with the current result set
        res &= words
    
    # Early exit if no common words remain
    if not res:
        break

# Output the number of common words
print(len(res))
