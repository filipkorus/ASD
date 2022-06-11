def check_fit(x, y, knapsack):
	""":return: False if element does not fit to knapsack else tuple of starting coordinates and boolean determining if element was turned (x, y, True/False)"""
	for x_start in range(len(knapsack) - x + 1):
		for y_start in range(len(knapsack) - y + 1):
			fits = True
			for x_iter in range(x):
				for y_iter in range(y):
					if knapsack[x_start + x_iter][y_start + y_iter] != 0:
						fits = False
						break
				if not fits:
					break
			if fits:
				return x_start, y_start, False

	# other orientation
	for x_start in range(len(knapsack) - x + 1):
		for y_start in range(len(knapsack) - y + 1):
			fits = True
			for x_iter in range(x):
				for y_iter in range(y):
					if knapsack[y_start + y_iter][x_start + x_iter] != 0:
						fits = False
						break
				if not fits:
					break
			if fits:
				return x_start, y_start, True

	return False
