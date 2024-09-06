def longest_prefix_suffix(S):
    n = len(S)
    if n == 1:
        return -1

    # Create the prefix array
    prefix = [0] * n
    j = 0  # Length of the previous longest prefix suffix

    for i in range(1, n):
        # Update j while there is a mismatch
        while j > 0 and S[i] != S[j]:
            j = prefix[j - 1]

        # If there is a match, increment j
        if S[i] == S[j]:
            j += 1
            prefix[i] = j

    # The last value in prefix array gives the longest prefix which is also a suffix
    result = prefix[-1]

    # If result is 0, there is no such prefix and suffix
    return result if result > 0 else -1

# Input
S = input().strip()

# Output
print(longest_prefix_suffix(S))
