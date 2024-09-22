def solve_lamp_grid(R, C, queries):
    # Initialize the grid using a list of integers
    # Each integer represents a row, with bits representing lamp states
    grid = [0] * R

    for x, y in queries:
        # Adjust for 0-based indexing
        x -= 1
        y -= 1
        
        # Toggle the entire row
        grid[x] ^= (1 << C) - 1
        
        # Toggle the column in each row
        for i in range(R):
            grid[i] ^= 1 << (C - 1 - y)
        
        # Ensure the queried lamp is always ON
        grid[x] |= 1 << (C - 1 - y)

    # Convert the grid to the required output format
    return [format(row, f'0{C}b') for row in grid]

# Read input
R, C = map(int, input().split())
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Solve and print output
result = solve_lamp_grid(R, C, queries)
for row in result:
    print(row)

#-------------------------------------------------------------------------------------#
# Input: R and C
r, c = map(int, input().split())

# Initialize the grid with all lamps turned off (0)
grid = [[0] * c for _ in range(r)]

# Toggle counters for rows and columns
row_toggle = [0] * r
col_toggle = [0] * c

# Number of queries
q = int(input())

# Process each query
for _ in range(q):
    r1, c1 = map(int, input().split())
    
    # Adjust for 0-based indexing
    r1 -= 1
    c1 -= 1
    
    # Increment toggle counters for the row and column
    row_toggle[r1] ^= 1
    col_toggle[c1] ^= 1

# Output the final grid state
for i in range(r):
    for j in range(c):
        # Calculate the final state based on toggle counters
        grid[i][j] = (row_toggle[i] ^ col_toggle[j])
    
    # Print the result row by row
    print(*grid[i])

