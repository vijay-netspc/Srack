import math

# Function to get the factors of a number N
def get_factors(N):
    factors = []
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            factors.append(i)
            if i != N // i:
                factors.append(N // i)
    return sorted(factors)

# Function to fill the grid with inverted L-shaped layers
def fill_grid(N, factors):
    M = len(factors)
    grid = [[0] * M for _ in range(M)]
    
    # Filling the grid with inverted L-shaped layers
    for i in range(M):
        for row in range(i, M):
            grid[row][i] = factors[i]
        for col in range(i, M):
            grid[i][col] = factors[i]
    
    return grid

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

# Main function to read input and generate the grid
def main():
    N = int(input())  # Reading input N
    factors = get_factors(N)  # Getting factors of N
    grid = fill_grid(N, factors)  # Filling the grid
    print_grid(grid)  # Printing the grid

# Call the main function
main()

