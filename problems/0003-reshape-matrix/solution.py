import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	orig_shape = len(a) * len(a[0])
	if orig_shape != new_shape[0] * new_shape[1]:
		print(f"Matrix of shape {orig_shape} cannot be reshaped into f{new_shape}!")
		return list()
	else:
		one_dim_matrix = []
		for row in range(len(a)):
			for element in range(len(a[row])):
				one_dim_matrix.append(a[row][element])
		reshaped_matrix = []
		for j in range(0, len(one_dim_matrix), new_shape[1]):
			reshaped_matrix.append(one_dim_matrix[j:j+new_shape[1]])

	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	return reshaped_matrix