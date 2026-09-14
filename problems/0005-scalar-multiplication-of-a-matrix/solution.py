def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	for row in range(len(matrix)):
		for element in range(len(matrix[0])):
			matrix[row][element] *= scalar
	return matrix