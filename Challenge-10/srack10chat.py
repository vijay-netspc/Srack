from bisect import bisect_right

# Input list of unique integers
lst = list(map(int, input().strip().split()))

# Sort the list
sorted_lst = sorted(lst)

# Create a dictionary to map each number to the next greater element
next_greater = {}

for i in range(len(sorted_lst)):
    # Use binary search to find the next greater element
    index = bisect_right(sorted_lst, sorted_lst[i])
    if index < len(sorted_lst):
        next_greater[sorted_lst[i]] = sorted_lst[index]
    else:
        next_greater[sorted_lst[i]] = -1

# Output the results for each element in the original list
output = [str(next_greater[num]) for num in lst]
print(" ".join(output))
