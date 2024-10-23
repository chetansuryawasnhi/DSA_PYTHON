import numpy as np
def extract_3x3_submatrices(big_matrix):
    m, n = big_matrix.shape
    submatrices = []

    for i in range(0, m - 2, 3):  # Step by 3 rows
        for j in range(0, n - 2, 3):  # Step by 3 columns
            # Extract the 3x3 submatrix starting at (i, j)
            submatrix = big_matrix[i:i+3, j:j+3]
            submatrices.append(submatrix)

    return submatrices

# Example usage:

big_matrix = np.random.rand(9, 9)  # Example 9x9 matrix
submatrices = extract_3x3_submatrices(big_matrix)
print(submatrices)

# Each element in submatrices will be a 3x3 numpy array
