# import numpy as np

def matrix_dot_vector(matrix, vector):
	if len(matrix[0]) != len(vector):
		return -1
	else:
		return([sum([i * j for i, j in zip(row, vector)]) for row in matrix])
	# pass
