def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	cov_matrix = [[[] for i in range(len(vectors))] for j in range(len(vectors))]
	n = len(vectors[0]) - 1
	for f1 in range(len(vectors)):
		for f2 in range(len(vectors)):
			mean_f1 = sum(vectors[f1]) / len(vectors[f1])
			mean_f2 = sum(vectors[f2]) / len(vectors[f2])
			products = [(i - mean_f1) * (j - mean_f2) for i,j in zip(vectors[f1], vectors[f2])]
			sum_of_products = sum(products)
			cov_matrix[f1][f2] = sum_of_products/n
	return cov_matrix