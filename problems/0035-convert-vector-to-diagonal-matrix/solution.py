import numpy as np

def make_diagonal(x):
	result = []
	for element in range(len(x)):
		result.append([0 if i != element else float(x[element]) for i in range(len(x))])

	return result