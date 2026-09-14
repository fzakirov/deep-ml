import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        return None
    else:
        a_inv = np.zeros((2,2)).tolist()
        term = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
        for i in range(2):
            for j in range(2):
                a_inv[i][j] = term[i][j]*(1/det)

        return a_inv
