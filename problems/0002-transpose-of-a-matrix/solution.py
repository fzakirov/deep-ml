def transpose_matrix(matrix):
    return(
        [[row[idx] for row in matrix] for idx in range(len(matrix[0]))]
    )
	