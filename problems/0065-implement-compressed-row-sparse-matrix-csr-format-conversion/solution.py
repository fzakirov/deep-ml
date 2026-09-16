import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	
	vals = []
	col_idx = []
	row_ptr = []
	non_zero_cnt = 0
	row_ptr.append(0)
	for row_id in range(len(dense_matrix)):
		for col_id in range(len(dense_matrix[row_id])):
			value = dense_matrix[row_id][col_id]
			if value !=0:
				vals.append(value)
				col_idx.append(col_id)
				non_zero_cnt += 1
		row_ptr.append(non_zero_cnt)

	return vals, col_idx, row_ptr
