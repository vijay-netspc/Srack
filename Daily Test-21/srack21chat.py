# Accepting the inputs
N = int(input())
P = int(input())
Q = int(input())

# Initialize the count to track occurrences of Q
count = 0

# Loop through P iterations and check if Q is in the sum
for i in range(1, P + 1):
    current_sum = N + i * P
    if str(Q) in str(current_sum):
        count += 1

# Print the final count
print(count)
