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
