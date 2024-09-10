n = int(input())
arr = [int(i) for i in input().split()]

for i in range(0, n, 3):
    digits = [arr[i] % 10, arr[i+1] % 10, arr[i+2] % 10]
    
    # Sort digits in descending order
    digits_sorted = sorted(digits, reverse=True)
    
    # Check if the largest number starts with 0
    if digits_sorted[0] == 0:
        print(-1, end=" ")
    else:
        # Combine the digits to form the largest possible three-digit number
        largest_number = ''.join(map(str, digits_sorted))
        print(largest_number, end=" ")
