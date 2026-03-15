def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == "row":
		for row in matrix:
			row_mean = sum(row) / len(row)
			means.append(row_mean)
	elif mode == "column":
		for col_id in range(len(matrix[0])):
			col_mean = sum([row[col_id] for row in matrix]) / len([row[col_id] for row in matrix])
			means.append(col_mean)
	return means