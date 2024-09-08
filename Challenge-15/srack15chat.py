def find_pairs_with_sum():
    # Read the input
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Store the numbers in a set for quick lookups
    num_set = set(arr)
    
    # To store the valid pairs
    result = []
    
    # Find pairs whose sum exists in the set
    for i in range(n):
        for j in range(i + 1, n):
            pair_sum = arr[i] + arr[j]
            if pair_sum in num_set:
                result.append((arr[i], arr[j], pair_sum))
                result.append((arr[j], arr[i], pair_sum))  # Include reversed pair
    
    # If no pairs found, print -1
    if not result:
        print(-1)
        return
    
    # Sort the result by sum, then by the first operand
    result.sort(key=lambda x: (x[2], x[0]))
    
    # Print the sorted pairs in the required format
    for pair in result:
        print(f"{pair[0]} + {pair[1]} = {pair[2]}")

# Run the function
find_pairs_with_sum()
