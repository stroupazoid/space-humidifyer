import itertools

def is_associative(matrix):
    """Checks if a 3x3 Cayley table is associative."""
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if matrix[matrix[i][j]][k] != matrix[i][matrix[j][k]]:
                    return False
    return True

def print_associative_matrices(limit=20):
    # Generate all possible rows (27 total)
    row_possibilities = list(itertools.product([0, 1, 2], repeat=3))
    
    # Generate all possible 3x3 matrices (19,683 total)
    all_matrices = itertools.product(row_possibilities, repeat=3)
    
    count = 0
    print(f"Printing the first {limit} associative 3x3 matrices:\n")
    
    for matrix in all_matrices:
        if is_associative(matrix):
            count += 1
            
            # Print the matrix nicely formatted
            print(f"Matrix #{count}:")
            for row in matrix:
                # Formats the row to look like [0, 1, 2]
                print(f"  {list(row)}")
            print() # Blank line between matrices
            
            # Stop printing if we reach the limit
            if count == limit:
                print(f"--- Stopped printing at the limit of {limit} ---")
                break

# Run the function
# Change the number to control how many you want to see (e.g., limit=113)
print_associative_matrices(limit=20)
