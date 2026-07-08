import itertools

def is_associative(matrix):
    """Checks if a 3x3 Cayley table is associative."""
    # Since n=3 is fixed, we can just use range(3)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if matrix[matrix[i][j]][k] != matrix[i][matrix[j][k]]:
                    return False
    return True

def analyze_all_3x3_matrices():
    # Generate all possible choices for a single row (3^3 = 27 variations)
    row_possibilities = list(itertools.product([0, 1, 2], repeat=3))
    
    # Generate all possible 3x3 matrices by combining 3 rows (27^3 = 19,683 variations)
    all_matrices = itertools.product(row_possibilities, repeat=3)
    
    associative_count = 0
    total_count = 0
    
    print("Analyzing all 3x3 matrices with entries {0, 1, 2}...\n")
    
    for matrix in all_matrices:
        total_count += 1
        if is_associative(matrix):
            associative_count += 1
            # Optional: Print the first few associative matrices found
            if associative_count <= 3:
                print(f"Associative Matrix #{associative_count}:")
                for row in matrix:
                    print(list(row))
                print("-" * 20)
                
    print("=" * 30)
    print(f"Analysis Complete.")
    print(f"Total matrices checked: {total_count:,}")
    print(f"Total associative matrices found: {associative_count:,}")

# Run the analysis
analyze_all_3x3_matrices()
