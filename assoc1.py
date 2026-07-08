def is_associative(matrix):
    """
    Checks if a square matrix representing a Cayley table is associative.
    
    Parameters:
    matrix (list of list of int): An n x n matrix where elements are 0-indexed 
                                 and represent the result of the operation.
    
    Returns:
    bool: True if associative, False otherwise.
    """
    n = len(matrix)
    
    # Quick validation: Ensure it's a square matrix
    for row in matrix:
        if len(row) != n:
            raise ValueError("The matrix must be square (n x n).")
            
    # Check the associativity condition for every triplet (i, j, k)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # (i * j) * k
                left_side = matrix[matrix[i][j]][k]
                # i * (j * k)
                right_side = matrix[i][matrix[j][k]]
                
                if left_side != right_side:
                    # Optional: Print the counterexample for debugging
                    # print(f"Fails for triplet ({i}, {j}, {k}): ({i}*{j})*{k} != {i}*({j}*{k})")
                    return False
                    
    return True

# --- Example Usage ---

# Example 1: A known associative table (Klein Four-group)
# Elements mapped to 0, 1, 2, 3
klein_four = [
    [0, 1, 2, 3],
    [1, 0, 3, 2],
    [2, 3, 0, 1],
    [3, 2, 1, 0]
]

# Example 2: A non-associative table 
non_associative = [
    [1, 2, 0],
    [0, 1, 2],
    [2, 0, 1]
]

print("Is Klein Four-group associative?", is_associative(klein_four))      # Expected: True
print("Is the second table associative?", is_associative(non_associative)) # Expected: False
