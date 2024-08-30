n = int(input())
lst = [int(i) for i in input().strip().split()]
k = int(input())

# Initial sum of the first subarray of length k
current_sum = sum(lst[:k])
min_sum = current_sum
min_index = 0

# Sliding window to find the subarray with the minimum sum
for i in range(1, n - k + 1):
    # Update the sum by subtracting the element that is left behind 
    # and adding the new element in the current window
    current_sum = current_sum - lst[i - 1] + lst[i + k - 1]
    
    # Update the minimum sum and index if a new minimum is found
    if current_sum < min_sum:
        min_sum = current_sum
        min_index = i

# Output the subarray with the minimum sum
print(*lst[min_index:min_index + k])
